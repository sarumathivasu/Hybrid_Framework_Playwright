import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL=os.getenv("BASE_URL")
EMPLOYEE_LIST_PIM_URL=os.getenv("EMPLOYEE_LIST_PIM_URL")