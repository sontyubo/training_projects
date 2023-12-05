from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

from .forms import RegisterForm, LoginForm

# Create your views here.
class RegisterView(View):
    def get(self, request, *args, **kwargs):
        # すでにログインしている場合はリダイレクト
        if request.user.is_authenticated:
            return redirect(reverse('shopTip:index'))
        
        context = {
            'form':RegisterForm(),
        }
        return render(request, 'register.html', context)
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'register.html', {'form':form})
        

        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        # ユーザーオブジェクトを保存
        user.save()

        auth_login(request, user)
        
        # 疑問点
        return redirect(reverse('shopTip:index'))

class LoginView(View):
    def get(self, request, *args, **kwargs):
        # すでにログインしている場合はリダイレクト
        if request.user.is_authenticated:
            return redirect(reverse('shopTip:index'))
        
        context = {
            'form':LoginForm()
        }
        
        return render(request, 'login.html', context)
    
    def post(self, request, *args, **kwargs):
        # リクエストからフォームを作る
        form = LoginForm(request.POST)

        if not form.is_valid():
            return render(request, 'login.html', {'form':form})
        
        # ログイン処理
        username = form['username'].value()
        password = form['password'].value()
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # ログイン処理
            auth_login(request, user)

        # ログイン後処理

        # ロギング

        # メッセージ表示
        messages.info(request, "Now login")
        
        return redirect(reverse('shopTip:index'))
    

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        # ログインしている場合はログアウト
        if request.user.is_authenticated:
            # ロギング

            # ログアウト処理
            auth_logout(request)

        # メッセージを表示
        messages.info(request, 'Now logout')
        
        return redirect(reverse('accounts:login'))