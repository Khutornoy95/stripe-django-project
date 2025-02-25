# Stripe Django Project

Это тестовое задание. Проект позволяет создавать платежные формы для товаров и обрабатывать платежи через Stripe Checkout.

## Функционал
- Модель `Item` для хранения информации о товарах.
- API для создания Stripe Checkout Session.
- HTML страница с кнопкой для оплаты товара.

## Установка и запуск

1. Клонирование репозитория
git clone https://github.com/Khutornoy95/stripe-django-project.git
cd stripe-django-project

2. Запуск с использованием Docker
Убедитесь, что у вас установлены Docker и Docker Compose.

Создайте файл .env в корне проекта и добавьте Stripe ключи:

STRIPE_PUBLIC_KEY=pk_ваш_публичный_ключ
STRIPE_SECRET_KEY=sk_ваш_секретный_ключ

Соберите и запустите контейнер:

docker-compose up --build
Приложение будет доступно по адресу: http://localhost:8000.

3. Запуск без Docker
Установите зависимости:

pip install -r requirements.txt
Создайте файл .env и добавьте Stripe ключи (см. выше).

Примените миграции:

python manage.py migrate
Запустите сервер:

python manage.py runserver