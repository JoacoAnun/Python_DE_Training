import sys

from analyzer import analyze_data
from logger import get_logger

logger = get_logger(__name__)

if __name__ == "__main__":
    logger.info("Starting Analisis.")
    result = analyze_data()
    logger.debug("Analisis result: %s", result)
    logger.info("Analisis Finished.")

    if result == "No files to process":
        # Finish program with no error
        logger.info("Nothing to process.")
        sys.exit(0)

    for key, value in result.items():
        logger.debug("%s %s", key, value)
