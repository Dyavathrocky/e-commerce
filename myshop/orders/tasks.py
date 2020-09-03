from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    #to send email to customer
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {Order.id}'
    message = f'Dear {order.first_name},\n\n' \
        f'you have successfully placed an order.' \
            f'your order id is {Order.id}.'
    mail_sent = send_mail(subject,message, 'davathrak@gmail.com', [order.email])
    return mail_sent