from tortoise import fields, models
from datetime import datetime
from app.models.order import Order

class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=20)
    orders: fields.ReverseRelation["Order"]
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        table = "users"