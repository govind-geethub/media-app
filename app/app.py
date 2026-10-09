from fastapi import FastAPI

app = FastAPI()

text_posts = {1 : {"title": "New Post", "content": "cool test post"}}

@app.get("/posts")
def get_all_posts() :
    return text_posts

@app.get("/posts/{id}")
def get_post(id : int) :
    return text_posts.get(id)