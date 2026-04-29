from fastapi import FastAPI

app = FastAPI(version="0.0.24")
@app.get("/")
def read_app():
    return {"Hello": "FastAPi"}

# Health check endpoint
@app.get("/health")
def get_health():
    return {"status":"ok"}
# Version endpoint
@app.get("/version")
def get_version():
    return {"version": app.version}  