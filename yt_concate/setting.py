import os
from dotenv import load_dotenv  # save the api_key in .env using detenv package
load_dotenv()                   # we can save api_key in our pc enviroment

API_KEY = os.getenv('API_KEY')