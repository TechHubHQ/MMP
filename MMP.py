# ===========================================================================
# Imports/Packages
# ===========================================================================
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
# from Connections.MPconDBConnector import GetDBConnection

# Logging Configurations
logger.add("logs/MMP.log", rotation="1 week", retention="1 week", compression="zip", enqueue=True)

# Initialize FastAPI
app = FastAPI()

origins = [
    "http://localhost:5174",
    "*"
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/api/v1/test")
async def test():
    logger.info("API Call Test Passed")
    return {"message": "API Call Test Passed"}
