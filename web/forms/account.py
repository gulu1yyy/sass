from django import forms
from web.models import UserInfor
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django_redis import get_redis_connection


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(label="确认密码",widget=forms.PasswordInput())
    phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
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

class SendSmsForm(forms.Form):
    phone = forms.CharField(label="手机号",validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'),])
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        tpl = self.request.GET.get("tpl")
        if tpl:
            pass
        exits = UserInfor.objects.filter(phone=phone).exists()
        if exits:
           raise ValidationError("手机号已存在")
        code = 1234

        return phone
    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.request = request
