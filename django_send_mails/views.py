from django.shortcuts import render, redirect
from django.views import View
from django_send_mails.forms import EmailForm
from django_send_mails.utils.mail import *

class Index(View):
    template_name = "django_send_mails/index.html"
    context = {}
    
    def get(self, request, *args, **kwargs):
        form = EmailForm()
        self.context["form"] = form
        self.context["title"] = "Send Mail"
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            
            try:
                # send_mail_default1(form.cleaned_data)
                send_mail_default2(form.cleaned_data)
                # send_mail_HTML1(form.cleaned_data)
                # send_mail_HTML2(form.cleaned_data)
                return redirect('django_send_mails:index')
            except Exception as e:
                errors = form._errors.setdefault("Email Error", ErrorList())
                errors.append("Failed to send the email")
                print(e)
        self.context["form"] = form
        return render(request, self.template_name, self.context)