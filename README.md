# Simple Social Media App

A full-stack social media web application built with **Python, FastAPI, and Streamlit**. Users can register, authenticate securely, upload images and videos with captions, and explore posts shared by other users. The application uses **PostgreSQL** for persistent data storage and **ImageKit** for cloud media hosting.

## 🚀 Live Demo

**[Try Simple Social Media](https://simple-social-media-2llfbmftumrfe4rptoogst.streamlit.app/)**

## ✨ Features

- **User Authentication:** User registration and login with JWT-based authentication using FastAPI Users.
- **Media Sharing:** Upload images and videos with captions.
- **Social Feed:** Browse posts with media, captions, author information, and timestamps.
- **Post Management:** Delete your own posts with backend ownership verification.
- **Cloud Media Storage:** Store and serve uploaded media through ImageKit.
- **Persistent Database:** Store user accounts and post metadata in PostgreSQL.
- **Database Migrations:** Manage database schema changes using Alembic.
- **REST API:** Expose backend functionality through FastAPI endpoints.

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python, FastAPI |
| Authentication | FastAPI Users, JWT |
| Database | PostgreSQL |
| ORM | SQLAlchemy (async) |
| Media Storage | ImageKit |
| Database Migrations | Alembic |
| HTTP Client | Requests |
| Backend Hosting | Render |
| Frontend Hosting | Streamlit Community Cloud |

## 🏗️ Architecture

1. Users interact with the Streamlit frontend.
2. The frontend sends HTTP requests to the FastAPI backend.
3. FastAPI handles authentication, post operations, and authorization.
4. SQLAlchemy communicates asynchronously with PostgreSQL to manage users and post metadata.
5. ImageKit stores uploaded media and provides URLs used to display it in the feed.

## ⚙️ Run Locally

### Prerequisites

- Python 3.10 or later (use a version compatible with your installed dependencies)
- Git

### 1. Clone the repository

```bash
git clone https://github.com/govind-geethub/simple-social-media.git
cd simple-social-media
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and configure the variables required by the backend, including your database URL, JWT secret, and ImageKit credentials.

**Never commit `.env` or expose secret keys in your repository.**

### 5. Start the backend

Run the FastAPI application using the command appropriate for your project configuration. For example:

```bash
uvicorn app.app:app --reload
```

### 6. Start the frontend

In a separate terminal, run:

```bash
streamlit run frontend.py
```

Ensure the frontend's `API_URL` points to your local backend when developing locally.

## 🔐 Security

- JWT-based authentication for protected operations.
- Backend authorization checks for post deletion.
- Environment variables for sensitive credentials.
- Database schema management with Alembic.

## 👨‍💻 Author

**Govind Kumar**

- GitHub: [govind-geethub](https://github.com/govind-geethub)

---

If you find this project useful, consider giving the repository a ⭐.
