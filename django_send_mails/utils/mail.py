from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.forms.utils import ErrorList
from django.core.mail import EmailMultiAlternatives

def send_mail_default1(data):
    send_mail(
        data['subject'],
        data['message'],
        "django.mails@example.com",
        [data['receiver']],
    )

def send_mail_default2(data):
    # Build message
    email = EmailMessage(
        subject=data['subject'],
        body=data['message'],
        from_email="django.mails@example.com",
        to=[data['receiver']],
        bcc=['eranthaw@atlinkcom.com'], 
        cc=['eranthawelikala@gmail.com'],
        headers = {'Reply-To': 'support@django.mails.com'})
    # Send message with built-in send() method
    email.send()

def send_mail_HTML1(data):
    subject, from_email, to = data['subject'], "django.mails@example.com", data['receiver']
    text_content = data['message']
    html_content = "<h1>{message}</h1>".format(message=data['message'])
    msg = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email, to=[to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_mail_HTML2(data):
    subject, from_email, to = data['subject'], "django.mails@example.com", data['receiver']
    html_content = "<h1>{message}</h1>".format(message=data['message'])
    msg = EmailMessage(subject=subject, body=html_content, from_email=from_email, to=[to])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
