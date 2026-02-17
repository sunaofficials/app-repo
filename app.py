from fastapi import FastAPI
import os

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION", "v1")

@app.get("/")
def root():
    return {
        "message": "Hello from Cisco MCN Multi-Cloud Demo 🚀",
        "version": APP_VERSION
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
