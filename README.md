# 🚀 Microservices Project (Django + FastAPI + PostgreSQL + Docker)

Ushbu repository **tayyor microservice arxitekturasi** bo‘lib, quyidagi texnologiyalarni o‘zida birlashtiradi:

- **Django (DRF)** — Backend Admin / Core API  
- **FastAPI** — High-speed service (Auth, ML, External API, Background jobs…)  
- **PostgreSQL** — Bitta umumiy database  

- **Docker + Docker Compose** — Projectni 1 ta komandada ishga tushirish  
- **Production-ready arxitektura** (volumes, env, optimized Dockerfiles)

---

# 📁 Project Structure
```bash 
📦 MicroFastDRF/
├── docker-compose.yml
├── Dockerfile
├── src/
│ ├── django_app/
│ ├── manage.py
│ ├──apps/...
├ ├
│ ├── fastapi_app/
│ ├── main.py
│ ├── api/
│ └── services/...
├── .env
└── README.md
```

# 🚀 Arxitektura Konsepsiyasi

Ushbu loyiha **Hybrid Microservices Architecture** tamoyiliga asoslangan bo‘lib, Django va FastAPI birgalikda bitta PostgreSQL bazasi ustida ishlaydi.

---

## 🟦 Django (Core Service)

Django xizmatining asosiy vazifalari:

- **Model yaratadi**  
- `makemigrations` va `migrate` orqali **table yaratadi**  
- Django **Admin panel** beradi  

> Django – ma’lumotlar arxitekturasini belgilovchi “asosiy service”.

---

## 🟩 FastAPI (High-Performance Service)

FastAPI servisining vazifalari:

- Django yaratgan **table-lar bilan CRUD** operatsiyalar qiladi  
- SQLAlchemy orqali **to‘g‘ridan-to‘g‘ri PostgreSQL** bilan ishlaydi  
- Django model kodini ishlatmaydi, faqat **table structure** asosida ishlaydi  
- `Alembic` **kerak emas**, 

> FastAPI – Django model bazasiga ulanish orqali alohida microservice sifatida ishlaydi.

---

## 🗄 PostgreSQL (Shared Database)

PostgreSQL servisi:

- Django va FastAPI uchun **umumiy database**  
- Docker orqali konteyner sifatida boshqariladi  
- Fayllar **volume** orqali saqlanadi  
- Istalgan vaqtda TablePlus, DBeaver orqali ulanish mumkin:
