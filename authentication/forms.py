from datetime import timedelta

from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class UserCacheMixin:
    user_cache = None


class SignIn(UserCacheMixin, forms.Form):
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # if settings.USE_REMEMBER_ME:
        #     self.fields['remember_me'] = forms.BooleanField(label=_('Remember me'), required=False)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise ValidationError(_('You entered an invalid password.'))

        return password
#
#
class SignInViaUsernameForm(SignIn):
    username = forms.CharField(label=_('Username'))

    @property
    def field_order(self):
        # if settings.USE_REMEMBER_ME:
        #     return ['username', 'password', 'remember_me']
        return ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']

        user = User.objects.filter(username=username).first()
        if not user:
            raise ValidationError(_('You entered an invalid username.'))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user

        return username

class SignInViaEmailOrUsernameForm(SignIn):
    email_or_username = forms.CharField(label=_('Email or Username'))

    @property
    def field_order(self):
        # if settings.USE_REMEMBER_ME:
        #     return ['email_or_username', 'password', 'remember_me']
        return ['email_or_username', 'password']

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data['email_or_username']

        user = User.objects.filter(Q(username=email_or_username) | Q(email__iexact=email_or_username)).first()
        if not user:
            raise ValidationError(_('You entered an invalid email address or username.'))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user

        return email_or_username

class ArticleContextForm(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    _id = forms.CharField(label='??????id',max_length=50);#??????id(id)
    totallevel = forms.CharField(label='total??????',max_length=50);#total??????(totalLevel)
    typeid = forms.CharField(label='????????????id',max_length=50);#????????????id(typeid)  typeid=1 ????????????   typeid=2 ???????????? typeid=3 ??????????????????
    modelid = forms.CharField(label='????????????id',max_length=50);#????????????id(modelid)
    arcrank = forms.CharField(label='??????',max_length=50);#??????(arcrank)
    click = forms.CharField(label='??????',max_length=50);#??????(click)
    title = forms.CharField(label='????????????',max_length=50);#????????????(title)
    shortitle = forms.CharField(label='???????????????',max_length=50);#???????????????(shortitle)
    writer = forms.CharField(label='??????',max_length=50);#??????(writer)
    resource = forms.CharField(label='??????',max_length=50);#??????(resource)
    updatedate = forms.CharField(label='????????????',max_length=50);#????????????(updatedate)
    sendate = forms.CharField(label='????????????',max_length=50);#????????????(sendate)
    keywords = forms.CharField(label='?????????',max_length=50);#?????????(keywords)
    content = forms.CharField(label='????????????',max_length=50);#????????????(content)
    contentimg1 = forms.CharField(label='????????????',max_length=50);#????????????(contentimg1)
    titleimg1 = forms.CharField(label='????????????',max_length=50);#????????????(titleimg1)
