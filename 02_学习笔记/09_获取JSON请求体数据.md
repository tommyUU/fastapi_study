![img.png](..%2Fimg%2Fimg.png)
```python
import uvicorn
from fastapi import FastAPI, Header, Body

app = FastAPI()


@app.get("/user")
def user(id, token=Header(None)):  # 自定义头部信息token，后端接受到token字段信息，就会在前端返回相同字段的值
    return {'id': id,
            'token': token}


@app.post("/login")
def login(data=Body(None)):
    return {'data': data}


if __name__ == '__main__':
    uvicorn.run(app)

```