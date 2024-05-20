from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from web.forms.account import RegisterForm,SendSmsForm
# Create your views here.


def register(request):
    '''注册界面'''
    form = RegisterForm()
    return render(request,"register.html", context={"form": form})

def send_sms(request):
    '''发送短信'''
    form = SendSmsForm(request=request,data=request.GET)
    #检验手机号是否为空，格式是否正确
    if form.is_valid():
        print(form.clean_phone())
        return JsonResponse({"status":True})
    else:
        return JsonResponse({"status":False,"errors":form.errors})