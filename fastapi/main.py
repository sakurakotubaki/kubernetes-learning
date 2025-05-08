from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="FastAPI Hello World",
    description="A simple FastAPI example deployed on Kubernetes",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello World from FastAPI on Kubernetes!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)