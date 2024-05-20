from django.shortcuts import render
from django import forms
from web.models import UserInfor
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your views here.


class SassForm(forms.ModelForm):
    confirm_password = forms.CharField(label="确认密码",widget=forms.PasswordInput())
    phone = forms.CharField(label="手机号", validators=[RegexValidator(r'/^1[3,4,5,7,8][0-9]{9}$/',"手机号格式错误")])
    password = forms.CharField(label="密码",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    code = forms.CharField(label="验证码")

    class Meta:
        fields = ['username','email','password','confirm_password','phone','code']
        model = UserInfor


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = "请输入"+f"{field.label}"


def register(request):
    form = SassForm()
    return render(request,"register.html", context={"form": form})