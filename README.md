# ecommerce_setup

Полнофункциональное Django-приложение для онлайн-магазина, развёрнутое с помощью Docker, Gunicorn, NGINX и PostgreSQL.

---

## 📦 Стек технологий

- Django + DRF
- PostgreSQL
- Gunicorn
- NGINX
- Docker + Docker Compose

---

## 🚀 Быстрый запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/Abdullaazimovs/onlinestore.git
cd onlinestore
```

### 2 Заполни .env файл

DB_NAME=onlinestore
DB_USER=postgres
DB_PASSWORD=yourpassword
SECRET_KEY=your-secret-key
DEBUG=0

### 3. Собери и запусти проект
```bash
docker compose up --build
```
