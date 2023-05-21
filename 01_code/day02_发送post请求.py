import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.api_route('/login', methods=['GET', 'POST', 'POST'])
def login():
    return {'msg': '登陆成功'}


if __name__ == '__main__':
    uvicorn.run(app)
