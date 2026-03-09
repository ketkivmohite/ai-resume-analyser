# Phase 1 Notes — Django Setup & Project Structure

## What I Learned in Phase 1

### Django Project Structure
- `manage.py` — command centre of the project
- `settings.py` — all configuration lives here
- `urls.py` — maps URLs to view functions
- `wsgi.py` / `asgi.py` — server entry points

### Apps vs Project
- Project = the whole thing (resume_ai/)
- App = one feature module (resumes, jobs, users)
- Each app has its own models, views, urls, templates

### Key Commands Learned
```bash
python manage.py runserver    # start server
python manage.py makemigrations  # create migration
python manage.py migrate      # apply migration
python manage.py shell        # Python shell with Django
```

### Bugs Fixed in Phase 1
- Fixed duplicate URL in resume_ai/urls.py
- Fixed requirements.txt (Django 6.0.2 → 5.1.7)
- Fixed missing .env file

### How MTV Works
- Model → defines data structure
- Template → HTML shown to user  
- View → logic connecting Model and Template

### What confused me at first
- Virtual environment activation on Windows
- Git setup — difference between clone vs init
- Why migrations need two commands