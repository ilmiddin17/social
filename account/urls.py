from django.urls import path,include,reverse_lazy
from . import views
from django.contrib.auth import views as auth_views



app_name='account'
urlpatterns=[
	#password reset urls
	path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

	#password reset urls
	path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('account:password_reset_done')), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
		success_url=reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	

	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), {'template_name': 'registration/logged_out.html'}, name='logout'),
	path('', views.dashboard, name='dashboard'),
]