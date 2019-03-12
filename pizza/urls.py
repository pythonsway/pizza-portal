"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.flatpages import views

from orders import views as order_views


# 'name' from base.html nav must match!
urlpatterns = [
    path('',
        include('orders.urls')),
    path('admin/',
        admin.site.urls),
    path('signup/',
        order_views.signup,
        name='signup'),
    path('login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'),
    path('logout/',
        auth_views.LogoutView.as_view(),
        name='logout'),
    path('reset/',
        auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html', email_template_name='registration/password_reset_email.html', subject_template_name='password_reset_subject.txt'),
        name='password_reset'),
    path('reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),
    path('settings/account/',
        order_views.UserUpdateView.as_view(),
        name='my_account'),
    path('settings/password/',
        auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
        name='password_change'),
    path('settings/password/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
        name='password_change_done'),
    path('about/',
        views.flatpage, {'url': '/about/'}, name='about')
    # path('account/', include('django.contrib.auth.urls'))
]

# django.contrib.auth.urls  :
# if not provided 'template_name': temlates/registration
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']