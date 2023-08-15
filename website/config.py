import os
from dotenv import load_dotenv

load_dotenv()
ENGINE = os.environ.get('ENGINE')[::]
NAME = os.environ.get('NAME')[::]
HOST = os.environ.get('HOST')[::]
PORT = os.environ.get('PORT')[::]
USER = os.environ.get('USER')[::]
PASSWORD = os.environ.get('PASSWORD')[::]
