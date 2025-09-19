from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_order_email(order_id):
    # Dummy example
    send_mail(
        subject=f"Order {order_id} Created",
        message="Your order has been successfully created.",
        from_email="noreply@ecommerce.com",
        recipient_list=["customer@example.com"]
    )
