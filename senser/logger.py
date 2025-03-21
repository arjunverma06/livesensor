import logging
import os
from datetime import datetime
import sys
log_file=f"{datetime.now().strftime('%m%d%Y%H%M%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(logs_path,exist_ok=True)
# log_path_join=os.join.path(logs_path,log_file)
log_path_join = os.path.join(logs_path, log_file)
logging.basicConfig(
    filename=log_path_join,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s-%(message)s",
  )