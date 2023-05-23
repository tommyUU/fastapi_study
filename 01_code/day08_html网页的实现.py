import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates('../03_pages')

todos = ['写日记', '看电影', '打飞机']


@app.get('/')
def index(req: Request, username):
    """
    主页，使用模板渲染网页
    :return:index.html，context
    """

    return template.TemplateResponse('index.html', context={'request': req, 'name': username, 'todos': todos}, )


@app.post('/todo')
def todo(todo=Form(None)):
    """
    处理用户发送的数据
    :return:
    """
    todos.insert(0, todo)
    return RedirectResponse('/?username=Abraham', status_code=302)


if __name__ == '__main__':
    uvicorn.run(app)
