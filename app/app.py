from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {1 : {"title": "New Post", "content": "cool test post"}}

@app.get("/posts")
def get_all_posts(limit: int = None) :
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id : int) :
    # error handling
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)