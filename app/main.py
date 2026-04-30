from fastapi import FastAPI
app = FastAPI(version="0.0.24")


# Root endpoint
@app.get("/")
def read_app():
    return {"Hello": "FastAPi"}

# Health check endpoint
@app.get("/health", status_code=200)
async def get_health():
    return {"status":"ok"}
# Version endpoint
@app.get("/version", status_code=200)
async def get_version():
    return {"version": app.version}  
