# Django Shop

Простой интернет-магазин на Django.

## Функциональность

- Главная страница
- Страница контактов
- Настроена маршрутизация

## Установка

1. Клонируйте репозиторий.
2. Создайте виртуальное окружение: 
```bash
   python -m venv venv
```

3. Активируйте его: 
(Windows)
```bash
`venv\Scripts\activate` 
``` 
 или (Linux/Mac).
```bash
source venv/bin/activate
```  
4. Установите зависимости: 
```bash
pip install -r requirements.txt
```

5. Запустите миграции: 
 ```bash
python manage.py migrate
```

6. Запустите сервер: 
 ```bash
python manage.py runserver
```

## Страницы

- `/` — главная
- `/contacts/` — контакты

## Лицензия

MIT