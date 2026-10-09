from fastapi import FastAPI

app = FastAPI(title="Media App API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "FastAPI is running successfully!"}