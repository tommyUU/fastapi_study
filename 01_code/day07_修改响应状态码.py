import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse

app = FastAPI()


@app.get('/user')  # JSONResponse返回的是JSON格式的文档
def user():
    return JSONResponse(content={'msg': 'get user'},
                        status_code=202,
                        headers={'a': 'b'})


@app.get('/')  # HTMLResponse返回的是HTML格式的文档
def user():
    html_content = """
    <html>
        <body><p style="color:red">Hello World</p></body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get('/img')
def user():
    img = r'D:\fastapi_study\img\02.png'
    # return FileResponse(img, filename='test.png')   填写filename会直接下载图片
    return FileResponse(img)  # 不会下载图片


if __name__ == '__main__':
    uvicorn.run(app)
