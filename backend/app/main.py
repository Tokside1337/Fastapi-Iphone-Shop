from importlib import reload
import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def main():
    return "Hello"

if __name__ == '__main__':
    uvicorn.run("main:app",reload = True)
