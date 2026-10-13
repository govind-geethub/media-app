import streamlit as st
import requests

API_URL = "https://simple-social-media-b9c4.onrender.com"


st.set_page_config(page_title="Simple Social", layout="wide")

st.markdown("""
<style>
/* Increase sidebar navigation text */
[data-testid="stSidebar"] [data-testid="stRadio"] label p {
    font-size: 20px !important;
}

/* Increase the navigation label */
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
    font-size: 20px !important;
}

/* Increase radio button size */
[data-testid="stSidebar"] [data-testid="stRadio"] label > div:first-child {
    transform: scale(1.25);
}
</style>
""", unsafe_allow_html=True)


# Initialize session state
if 'token' not in st.session_state:
    st.session_state.token = None
if 'user' not in st.session_state:
    st.session_state.user = None


def get_headers():
    """Get authorization headers with token"""
    if st.session_state.token:
        return {"Authorization": f"Bearer {st.session_state.token}"}
    return {}


def login_page():
    st.title("🚀 Welcome to Simple Social")

    # Simple form with two buttons
    email = st.text_input("Email:")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if email and password:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Login", type="primary", use_container_width=True):
                # Login using FastAPI Users JWT endpoint
                login_data = {"username": email, "password": password}
                response = requests.post(f"{API_URL}/auth/jwt/login", data=login_data)

                if response.status_code == 200:
                    token_data = response.json()
                    st.session_state.token = token_data["access_token"]

                    # Get user info
                    user_response = requests.get(f"{API_URL}/users/me", headers=get_headers())
                    if user_response.status_code == 200:
                        st.session_state.user = user_response.json()
                        st.rerun()
                    else:
                        st.error("Failed to get user info")
                else:
                    st.error("Invalid email or password!")


        with col2:
            if st.button("Sign Up", type="secondary", use_container_width=True):
                if not username.strip():
                    st.error("Please enter a username!")
                else:
                    signup_data = {
                        "email": email,
                        "username": username.strip(),
                        "password": password
                    }

                    response = requests.post(
                        f"{API_URL}/auth/register",
                        json=signup_data
                    )

                    if response.status_code == 201:
                        st.success("Account created! Click Login now.")
                    else:
                        error_detail = response.json().get(
                            "detail", "Registration failed"
                        )
                        st.error(f"Registration failed: {error_detail}")

    else:
        st.info("Enter your email and password above")


def upload_page():
    st.title("📸 Share Something")

    uploaded_file = st.file_uploader("Choose media", type=['png', 'jpg', 'jpeg', 'mp4', 'avi', 'mov', 'mkv', 'webm'])
    caption = st.text_area("Caption:", placeholder="What's on your mind?")

    if uploaded_file and st.button("Share", type="primary"):
        if not st.session_state.token:
            st.error("Your session has expired. Please log in again.")
            st.session_state.user = None
            st.rerun()
            return
        with st.spinner("Uploading..."):
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            data = {"caption": caption}
            response = requests.post(f"{API_URL}/upload", files=files, data=data, headers=get_headers())

            if response.status_code == 200:
                st.success("✅ Uploaded successfully! Go check out the Feed page.")
            else:
                st.error(f"Upload failed! Status: {response.status_code}")
                st.code(response.text)


def feed_page():
    st.title("🏠 Feed")

    response = requests.get(f"{API_URL}/feed", headers=get_headers())
    if response.status_code == 200:
        posts = response.json()["posts"]

        if not posts:
            st.info("No posts yet! Be the first to share something.")
            return

        for post in posts:
            st.markdown("---")

            # Header with user, date, and delete button (if owner)
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"**{post['email']}** • {post['created_at'][:10]}")
            with col2:
                if post.get('is_owner', False):
                    if st.button("🗑️", key=f"delete_{post['id']}", help="Delete post"):
                        # Delete the post
                        response = requests.delete(f"{API_URL}/posts/{post['id']}", headers=get_headers())
                        if response.status_code == 200:
                            st.success("Post deleted!")
                            st.rerun()
                        else:
                            st.error("Failed to delete post!")

            # Uniform media display with caption overlay
            caption = post.get('caption', '')
            col1, col2 = st.columns([1,1])
            with col1:
                if post['file_type'] == 'image':
                    st.image(post['url'], width = 250)
                else:
                    st.video(post['url'], width = 400)
            with col2:
                st.markdown("#### Caption")
                st.markdown(caption.replace("\n", "  \n"))

            st.markdown("")  # Space between posts
    else:
        st.error("Failed to load feed")


# Main app logic
if st.session_state.user is None:
    login_page()
else:
    # Sidebar navigation
    st.sidebar.title(f"👋 Hi {st.session_state.user['username']}!")

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.session_state.token = None
        st.rerun()

    st.sidebar.markdown("---")
    page = st.sidebar.radio("Navigate:", ["🏠 Feed", "📸 Upload"])

    if page == "🏠 Feed":
        feed_page()
    else:
        upload_page()