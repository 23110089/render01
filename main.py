from threading import Thread
from fastapi import FastAPI

def run(): import run
Thread(target=run).start()

app = FastAPI()
@app.get("/")
def home(): return 'Success'
