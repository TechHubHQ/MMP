# ===================================================================
# Imports/Packages
# ===================================================================
import time
import schedule
import psutil
from datetime import datetime
from loguru import logger

# Logging Configurations
logger.add("../logs/MPjLogSender.log", rotation="1 week", retention="1 week", compression='zip', enqueue=True)


# ===============================================================
# Sends Log files by compressing each directory
# ===============================================================
def SendLogs():
    try:
        logger.info("Sending Logs")
        logger.success("Logs sent")
    except Exception as e:
        logger.error(f"Error sending logs at {datetime.now()}: {e}")


# ===============================================================
# Logs PID and memory usage
# ===============================================================
def LogSystemInfo():
    process = psutil.Process()
    pid = process.pid
    # Memory usage in MB
    memory_usage = process.memory_info().rss / (1024 * 1024)
    logger.info(f"-- LogSender alive at PID: {pid}, Memory Usage: {memory_usage:.2f} MB --")


def LogSender():
    try:
        schedule.every(1).week.do(SendLogs)
        logger.info("LogSender started")
        while True:
            schedule.run_pending()
            LogSystemInfo()
            time.sleep(60)
    except KeyboardInterrupt:
        logger.error("LogSender stopped Manually")
    except Exception as e:
        logger.error(f"Error in LogSender: {e}")


if __name__ == "__main__":
    LogSender()
