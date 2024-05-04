# ===========================================================================
# Imports/Packages
# ===========================================================================
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from Connections.MPconDBConnector import CreateDB, GetDBConnection


# Logging Configurations
logger.add("logs/MMP.log", rotation="1 week", retention="1 week", compression="zip", enqueue=True)
CreateDB()

# Initialize FastAPI
app = FastAPI()

origins = [
    "http://localhost:5173",
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


# =============================================================
# Creates DB Connection if not exists, else returns None
# =============================================================

def CreateDBConnection():
    if GetDBConnection():
        logger.info("Database connection established")
        return None
    CreateDB()
    logger.info("Database created")
    return True

# =================================================================
# Connects to DB and returns the connection object
# =================================================================

def ConnectToDB():
    if not CreateDBConnection():
        logger.error("Error in creating database")
        return None
    db = GetDBConnection()
    return db


# ===================================================================
# Test API for checking if API is working
# ===================================================================

@app.get("/api/v1/test")
async def test():
    return {"message": "API Call Test Passed"}
