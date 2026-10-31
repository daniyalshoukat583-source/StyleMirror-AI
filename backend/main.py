from fastapi import FastAPI

app = FastAPI(
    title="StyleMirror AI",
    description="AI-powered Virtual Try-On and Fashion Designer",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to StyleMirror AI Backend!",
        "status": "Running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}