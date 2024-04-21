
# ========================================================
# Imports/Packages
# ========================================================
import os
import sqlite3
from loguru import logger
from contextlib import contextmanager


# Logging Configurations
logger.add("../logs/DBConnector.log", rotation="1 week", retention="1 week", compression='zip', enqueue=True)

# Variables
DB_NAME = "MMP.db"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "DataBase")
DB_PATH = os.path.join(DB_DIR, DB_NAME)


# =========================================================
# Create Database if not exists
# =========================================================

def CreateDB():
    try:
        if not os.path.exists(DB_PATH):
            with sqlite3.connect(DB_PATH):
                logger.info(f"Database created at {DB_PATH}")
    except Exception as e:
        logger.error(f"Error in creating database: {e}")


@contextmanager
def GetDBConnection():
    try:
        conn = sqlite3.connect(DB_PATH)
        yield conn
        conn.close()
        logger.info("Database connection closed")
    except Exception as e:
        logger.error(f"Error in getting database connection: {e}")
        raise e


if __name__ == "__main__":
    CreateDB()
