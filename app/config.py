import os
from dotenv import load_dotenv

load_dotenv()

SLEEPER_BASE_URL = os.getenv("SLEEPER_BASE_URL")
SPORT = os.getenv("SPORT")
SEASON = os.getenv("SEASON")



CACHE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data_cache')