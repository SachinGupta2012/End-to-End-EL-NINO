import logging
import os
from datetime import datetime

Log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
Log_path = os.path.join(os.getcwd(), "logs",Log_file)

os.makedirs(Log_path, exist_ok=True)

Log_path_file = os.path.join(Log_path, Log_file)

logging.basicConfig(
    filename=Log_path_file,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
if __name__ == "__main__":
    logging.info("Logging has been started.")