from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum  # Required for AWS Lambda/Vercel

app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse({"message": "Virtual TA is deployed on Vercel!"})

handler = Mangum(app)
