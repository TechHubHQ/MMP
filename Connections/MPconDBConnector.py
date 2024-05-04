
# ========================================================
# Imports/Packages
# ========================================================
import os
import sqlite3
from loguru import logger
from contextlib import contextmanager

# Variables
DB_NAME = "LensCraft.db"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "DataBase")
DB_PATH = os.path.join(DB_DIR, DB_NAME)


# =========================================================
# Create Database if not exists
# =========================================================
def CreateDB():
    try:
        if not os.path.exists(DB_PATH):
            if not os.path.exists(DB_DIR):
                os.makedirs(DB_DIR)
                logger.info("Database directory created")
            schema_path = os.path.join(DB_DIR, "schema.sql")
            with open(schema_path, "r") as f:
                logger.info("Creating database")
                schema = f.read()
            conn = sqlite3.connect(DB_PATH)
            conn.executescript(schema)
            logger.info("Database created")
        else:
            logger.info("Database file already exists")
    except Exception as e:
        logger.error(f"Error in creating database: {e}")


# =====================================================================
# Establish a DB Connection and return the connection object
# =====================================================================

@contextmanager
def GetDBConnection():
    try:
        conn = sqlite3.connect(DB_PATH)
        yield conn
    except Exception as e:
        logger.error(f"Error in getting database connection: {e}")
        raise e


if __name__ == "__main__":
    CreateDB()
