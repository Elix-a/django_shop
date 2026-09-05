from django.contrib import messages
from django.shortcuts import render


def home(request):
    """Контроллер главной страницы."""
    return render(request, "catalog/home.html")


def contacts(request):
    """
    Контроллер страницы контактов.
    При POST-запросе выводит сообщение об успешной отправке данных.
    """
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        message = request.POST.get("message", "")
        # Здесь можно сохранить данные в БД или отправить email.
        # Пока просто добавляем сообщение об успехе.
        messages.success(request, f"Спасибо, {name}! Ваше сообщение отправлено.")
    return render(request, "catalog/contacts.html")
