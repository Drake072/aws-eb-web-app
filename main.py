import time

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/slow-response")
def slow_response(seconds: int = Query(10,  description="The number of seconds to wait")):
    time.sleep(seconds)
    return {"message": f"slept {seconds} seconds"}