import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("reports/test.log"), logging.StreamHandler()])

logger = logging.getLogger()
