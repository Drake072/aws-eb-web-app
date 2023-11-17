import asyncio
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
async def slow_response(seconds: int = Query(10,  description="The number of seconds to wait")):
    start_time = time.time()
    await asyncio.sleep(seconds)
    end_time = time.time()
    return {"message": f"slept {seconds} seconds, overhead {(int)(end_time - start_time * 1000) - seconds * 1000} ms"}