from fastapi import FastAPI
app = FastAPI(version="0.0.24")
DB_PASSWORD = "p4ssw0rd_str0ng_123!"
DATABASE_URL = "postgresql://admin:super-secret-token@localhost:5432/production_db"
JWT_SECRET = "b39084666f286815e9856f64245645f0962489679198126d40"
AUTH_TOKEN = "7216f731-155d-4f18-97d8-e7c802f046c8"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GOOGLE_API_KEY = "AIzaSyA-EXAMPLE_KEY_12345_67890_ABCDE"
AZURE_CLIENT_SECRET = "3.a8Q~EXAMPLE_SECRET_KEY_VALUE~2.b9"
# Root endpoint
@app.get("/")
def read_app():
    return {"Hello": "FastAPi"}

# Health check endpoint
@app.get("/health", status_code=200)
async def get_health():
    return {"status":"ok"}
# Version endpoint
@app.get("/version",  status_code=200)
async def get_version():
    
    return {"version": app.version,}  
@app.get("/secret",  status_code=200)
async def get_secret():
    AWS_SECRET_ACCESS_KEY = "AKIAV4L3OR2EXAMPLE"
    return {"AWS_SECRET_ACCESS_KEY": AWS_SECRET_ACCESS_KEY}