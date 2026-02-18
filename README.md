# CollegeResultPortal

Simple Django app to lookup college student results and a minimal admin area.

Setup:

1. Create a Python virtualenv and activate it.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure MySQL credentials in `CollegeResultPortal/settings.py` (NAME, USER, PASSWORD, HOST, PORT).
4. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ to access the homepage.
