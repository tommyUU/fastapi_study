![img_1.png](..%2Fimg%2Fimg_1.png)
```python
import uvicorn
from fastapi import FastAPI, Header, Form

app = FastAPI()

@app.post("/login")
def login(username=Form(None), password=Form(None)):
    return {'data': {'username': username, 'password': password}}


if __name__ == '__main__':
    uvicorn.run(app)
```