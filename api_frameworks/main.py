from fastapi import FastAPI
import os
from routers import example

app = FastAPI()
app.include_router(example.router)


@app.get("/")
async def root():
    return {"Information":"This is my first API endpoint with FastAPI"}


if __name__ == "__main__":
    import uvicorn

    host = os.environ.get('HOST', "0.0.0.0")
    port = int(os.environ.get('PORT', 8000))

    uvicorn.run(app, host=host, port=port, reload=True)