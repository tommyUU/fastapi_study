import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise
from dao.models import Todo

app = FastAPI()
template = Jinja2Templates('../03_pages')

# 数据库的绑定
register_tortoise(app, db_url="mysql://root:Woaini8238!@119.96.166.24:3306/web_test_fastapi",
                  modules={"models": ["dao.models"]},
                  generate_schemas=True,
                  add_exception_handlers=True)

todos = ['写日记', '看电影', '打飞机']


@app.get('/')
async def index(req: Request, username):
    """
    从数据库获取 todos 的代码
    ORM模型， 获取所有的todos
    """

    todos = await Todo.all()

    return template.TemplateResponse('index.html', context={'request': req, 'name': username, 'todos': todos}, )


@app.post('/todo')
async def todo(content=Form(None)):
    """
    处理用户发送的数据
    :return:
    """
    # todos.insert(0, todo)
    # 把新的事项存储到数据库中
    await Todo(content=content).save()

    return RedirectResponse('/?username=Abraham', status_code=302)


if __name__ == '__main__':
    uvicorn.run(app)
