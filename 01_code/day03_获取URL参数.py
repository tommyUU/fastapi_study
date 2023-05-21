import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{id}")
def user(id):
    return {'id': id}


if __name__ == '__main__':
    uvicorn.run(app)
