import os
from dotenv import load_dotenv  # save the api_key in .env using detenv package

load_dotenv()                   # we can save api_key in our pc enviroment
API_KEY = os.getenv('API_KEY')

DOWNLOADS_DIR =  'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')# os.path.join == (downloads + videos)
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions') ## caption.txt will be saved to this dictionary

