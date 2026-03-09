#  AI Resume Analyzer
### *A Django + Python project built step by step — for learners, by a learner*



>  **This repo has two purposes:**
> 1. **Build** a real AI-powered resume analysis tool
> 2. **Teach** Django and Python through hands-on, phase-by-phase learning
>
> Whether you're here to use the app or learn to build it yourself — you're in the right place.



##  What This App Does

- 📄 Upload your resume as a PDF
- 🔍 Auto-extract all text from it
- 💼 Compare it against a job description
- 🤖 Get an AI-powered match score
- 📊 See a dashboard of your resume's strengths & gaps



##  Choose Your Path

###  Path 1: Just Run the App
Clone it, set it up, use it. See [Quick Start](#-quick-start) below.

###  Path 2: Learn Django by Building It
Follow the phases one by one. Each phase is a **separate Git branch** with:
- ✅ Working code
- 💬 Every line commented and explained
- 📖 A `PHASE_NOTES.md` teaching the concepts
- 🎯 Mini challenges to test your understanding

Start at [Phase 1](#-learning-path-phase-by-phase) →



##  Quick Start

### Prerequisites
Make sure you have these installed:
- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- A code editor — [VS Code](https://code.visualstudio.com/) recommended

### Setup Steps

```bash
# 1. Clone the repo
git clone https://github.com/ketkivmohite/ai-resume-analyser.git
cd ai-resume-analyser

# 2. Create a virtual environment
#    (Think of this as a clean room just for this project)
python -m venv venv

# 3. Activate the virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install all required libraries
pip install -r requirements.txt

# 5. Set up your environment variables
cp .env.example .env
# Open .env and fill in your values (see .env.example for guidance)

# 6. Set up the database
python manage.py migrate

# 7. Create an admin account (to access Django admin panel)
python manage.py createsuperuser

# 8. Run the server!
python manage.py runserver
```

Then open your browser and go to: **http://127.0.0.1:8000**

Admin panel: **http://127.0.0.1:8000/admin**



## Tech Stack

| Technology | What it does | Why we use it |
|---|---|---|
| **Python** | Main programming language | Readable, powerful, great for AI |
| **Django** | Web framework | Handles routing, database, auth for us |
| **SQLite** | Database (development) | Built into Python, zero setup needed |
| **PyMuPDF** | PDF text extraction | Fast and accurate PDF reading |
| **Git & GitHub** | Version control | Track changes, collaborate |

>  *As the project grows, we'll add: OpenAI API, PostgreSQL, and deployment tools.*



## Project Structure Explained

```
ai-resume-analyser/
│
├── apps/                        ← All the "departments" of our app
│   ├── analysis/                ←  AI analysis engine (Phase 4)
│   ├── jobs/                    ← Job listings (Phase 3)
│   ├── resumes/                 ←  Resume upload & storage (Phase 2)
│   └── users/                   ←  User accounts (Phase 3)
│
├── resume_ai/                   ← Project brain — settings & config
│   ├── settings.py              ← All configuration lives here
│   ├── urls.py                  ← Master list of all URL routes
│   ├── asgi.py / wsgi.py        ← Server entry points (ignore for now)
│
├── media/                       ← Uploaded PDF files are stored here
├── templates/                   ← HTML pages shown to users
├── manage.py                    ← Django's command-line tool
├── requirements.txt             ← All Python libraries this project needs
├── .env                         ← Your secret keys (never commit this!)
└── .env.example                 ← Template showing what .env needs
```

---

##  Learning Path: Phase by Phase

> Each phase is a **separate Git branch**. Switch branches to follow along!
> ```bash
> git checkout phase-1-setup     # Start here!
> ```

---

### Phase 1 — Django Setup & Project Structure
**Branch:** `phase-1-setup`

**What you'll learn:**
- What is Django and why use it?
- How to create a Django project from scratch
- What is a virtual environment and why it matters
- Understanding `settings.py`, `urls.py`, `manage.py`
- What are Django "apps" and how to create them

**What gets built:**
- Empty Django project
- 4 apps created: `resumes`, `jobs`, `users`, `analysis`
- Basic project configuration

📖 [Read Phase 1 Notes](notes/phase-1-notes.md)

---

###  Phase 2 — Resume Upload & PDF Text Extraction
**Branch:** `phase-2-resumes`

**What you'll learn:**
- What is a Django Model? (How data is structured)
- What is a Django View? (How requests are handled)
- What are URLs and how routing works
- How to handle file uploads in Django
- How to extract text from a PDF using PyMuPDF
- What is Django Admin and why it's powerful

**What gets built:**
- Resume upload form
- Automatic PDF text extraction on upload
- Resume stored in database with extracted text
- View all resumes in Django admin panel

 [Read Phase 2 Notes](notes/phase-1-notes.md)

---

###  Phase 3 — Jobs Module & User Accounts *(Coming Soon)*
**Branch:** `phase-3-jobs`

**What you'll learn:**
- Model relationships (ForeignKey — linking data together)
- User authentication in Django
- Forms and form validation
- Template inheritance (reusing HTML layouts)

**What gets built:**
- Add job descriptions to the system
- User registration & login
- Each user owns their own resumes

 Phase 3 Notes *(coming soon)*

---

###  Phase 4 — AI Analysis Engine *(Coming Soon)*
**Branch:** `phase-4-analysis`

**What you'll learn:**
- Calling external APIs from Django (OpenAI)
- Background tasks and processing
- Storing and displaying analysis results
- Django signals (auto-trigger actions)

**What gets built:**
- Extract skills from resumes automatically
- Compare resume skills vs job requirements
- Generate a match percentage score

 Phase 4 Notes *(coming soon)*

---

###  Phase 5 — Scoring & Results *(Coming Soon)*
**Branch:** `phase-5-scoring`

**What gets built:**
- Beautiful results page showing match score
- Skill gap analysis ("You're missing these skills")
- Resume improvement suggestions

---

### Phase 6 — Dashboard & Deployment *(Coming Soon)*
**Branch:** `phase-6-dashboard`

**What gets built:**
- Analytics dashboard
- Deployment to the web (so anyone can use it!)
- Production-ready settings

---

##  Django Concepts Quick Reference

> New to Django? Bookmark this section. You'll refer to it often.

### The Request-Response Cycle
```
User visits URL
      ↓
urls.py — "Which view handles this URL?"
      ↓
views.py — "Process the request, talk to database"
      ↓
models.py — "Here's how to read/write database data"
      ↓
templates/ — "Here's the HTML to show the user"
      ↓
User sees the page
```

### Key Django Files
| File | Purpose | Analogy |
|---|---|---|
| `models.py` | Define data structure | Blueprint of a form |
| `views.py` | Handle requests & responses | A waiter taking & delivering orders |
| `urls.py` | Map URLs to views | A restaurant menu / directory |
| `templates/` | HTML shown to users | The actual plate of food |
| `admin.py` | Register models for admin panel | Adding items to a management system |
| `settings.py` | All project config | The restaurant's rulebook |

---

##  Contributing

This is a learning project — contributions are welcome, especially:
-  Bug fixes
-  Better code comments / explanations
-  Improved notes for any phase
-  New features (open an issue first to discuss!)

### How to contribute:
```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
# Make your changes
git commit -m "Add: your clear commit message"
git push origin feature/your-feature-name
# Open a Pull Request!
```

---

##  About This Project

Built by **Ketki Mohite** as a hands-on way to learn Django and Python.

The goal: build something real, document the learning, and make it useful for other beginners too.

> *"The best way to learn is to build something you actually care about."*

---

##  Questions?

Open an [Issue](https://github.com/ketkivmohite/ai-resume-analyser/issues) — whether it's a bug, a question about the code, or a suggestion. All questions welcome! 

---

⭐ **If this helped you learn Django, give it a star!** It helps others find it too.