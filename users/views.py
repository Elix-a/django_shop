from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import UserRegisterForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Отправка приветственного письма
        send_mail(
            subject='Добро пожаловать!',
            message='Спасибо за регистрацию на нашем сайте.',
            from_email='noreply@shop.ru',
            recipient_list=[self.object.email],
            fail_silently=False,
        )
        return response


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ('avatar', 'phone_number', 'country')
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
