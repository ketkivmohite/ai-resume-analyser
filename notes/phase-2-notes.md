# Phase 2 Notes — Resume Upload & PDF Text Extraction

## What I Built in Phase 2

- forms.py — Django form for resume upload
- Upload view in views.py — handles GET and POST
- Upload URL in urls.py — /resumes/upload/
- resume_upload.html — the upload page template
- Fixed bug: resume.name → resume.title in detail template

## What I Learned

### Django Forms
- ModelForm builds a form automatically from a Model
- fields = [] controls which fields appear in the form
- form.is_valid() checks all fields before saving
- form.save() saves directly to database

### GET vs POST in a View
- GET → user visits the page → show empty form
- POST → user submits the form → process and save
- Always check request.method == 'POST' (uppercase!)

### File Uploads
- enctype="multipart/form-data" is required in HTML
- request.FILES holds the uploaded file
- Without enctype the PDF never reaches Django

### CSRF Token
- {% csrf_token %} must be in every POST form
- Django rejects any form without it
- It prevents fake form submissions

### PDF Text Extraction
- PyMuPDF (imported as fitz) reads PDF files
- Loop through pages → page.get_text()
- Triggered automatically in Resume model save()

## Bugs I Fixed
- 'Post' vs 'POST' — Python is case sensitive!
- Wrong indentation — else was inside if block
- Wrong URL prefix — resumes/ was missing in main urls.py

## Key Commands Used
python manage.py shell   # to test extraction worked
exit()                   # to exit the shell

## Git Workflow Used
git add .
git commit -m "message"
git push origin phase-2-resumes
git checkout main
git merge phase-2-resumes
git push origin main