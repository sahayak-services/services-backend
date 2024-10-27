from tortoise import fields, models
from app.models.service import Service

class Order(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="orders")
    service = fields.ForeignKeyField("models.Service", related_name="orders")

    status = fields.CharField(max_length=255, default="pending")
    

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"Order by {self.user_id} for {self.service_id}"  # Avoid accessing related fields directly in __str__

    class Meta:
        table = "orders"
