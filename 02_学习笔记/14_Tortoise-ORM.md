# register_tortoise

> `register_tortoise` 是 Tortoise-ORM 提供的一个函数，用于在 FastAPI 应用中注册和配置 Tortoise-ORM。Tortoise-ORM 是一个用于异步 Python 应用的 ORM（Object-Relational Mapping，对象关系映射）库。ORM 允许开发者使用面向对象的方式操作数据库，而不需要直接编写 SQL 语句。
>
> `register_tortoise` 需要三个主要参数：
>
> 1. `app`：这是你的 FastAPI 应用。
> 2. `db_url`：这是你的数据库连接字符串。它指定了数据库的类型（例如 MySQL 或 PostgreSQL）、用户名、密码、主机地址和数据库名称。
> 3. `modules`：这是一个字典，指定了你的模型（即数据库表的 Python 对象表示）所在的模块。
>
> `register_tortoise` 还有一些额外的可选参数，例如：
>
> * `generate_schemas`：如果设置为 True，则 Tortoise-ORM 会在启动时自动创建数据库表。这对于开发和测试很有用，但在生产环境中通常应该关闭。
> * `add_exception_handlers`：如果设置为 True，则 Tortoise-ORM 会为数据库错误添加异常处理程序。
>
> 在你的代码中，`register_tortoise` 被用于注册 Tortoise-ORM，并配置数据库连接和模型。这样，你就可以在其他部分的代码中使用 Tortoise-ORM 了，例如使用 `await Todo.all()` 来查询所有的待办事项，或使用 `await Todo(content=content).save()` 来保存一个新的待办事项。



# Tortoise-ORM

Tortoise-ORM 是一个异步的对象关系映射 (ORM) 工具，适用于 Python 中的 asyncio 与原生 SQL 数据库。在下面的内容中，我将通过一些例子来展示如何使用 Tortoise-ORM。

首先，你需要安装 Tortoise-ORM。你可以通过 pip 来安装：

```shell
pip install tortoise-orm
```

然后，你需要定义你的模型。这些模型会对应数据库中的表。例如，假设你有一个 `User` 表：

```python
from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)
    email = fields.CharField(max_length=50)

```

在上述代码中，`User` 类继承自 `Model` 类，并且定义了三个字段：`id`，`username` 和 `email`。这些字段会对应数据库中 `User` 表的列。

接下来，你需要初始化 Tortoise-ORM。你可以在你的程序启动时执行这个步骤：

```python
from tortoise import Tortoise

await Tortoise.init(
    db_url='sqlite://db.sqlite3',
    modules={'models': ['your_app.models']}
)
await Tortoise.generate_schemas()

```

在这段代码中，我们指定了数据库的 URL (`sqlite://db.sqlite3`)，以及包含我们模型的模块 (`your_app.models`)。然后，我们调用 `generate_schemas()` 方法来创建数据库表。

现在你已经准备好开始使用 Tortoise-ORM 了。以下是一些基本的 CRUD（创建、读取、更新、删除）操作的例子：

创建一个新的用户：

```python
user = await User.create(username='test', email='test@example.com')
```

读取一个用户：

```python
user = await User.get(id=1)

```

更新一个用户：

```python
await User.filter(id=1).update(username='new_test')

```

删除一个用户：

```python
await User.filter(id=1).delete()

```

以上只是 Tortoise-ORM 的一些基本操作，它还支持许多其他功能，如复杂的查询、关联和事务等。你可以在 [Tortoise-ORM 的文档](https://tortoise-orm.readthedocs.io/en/latest/) 中找到更多的信息。