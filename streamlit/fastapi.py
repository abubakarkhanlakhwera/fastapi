from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
def read_helloworld():
    return {"message": "Hello, World!"}

