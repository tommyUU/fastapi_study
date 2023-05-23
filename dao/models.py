from tortoise import Model, fields


class Todo(Model):
    """
    数据库中的表 todo
    """
    id = fields.IntField(pk=True)
    content = fields.CharField(max_length=500)
    created_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)