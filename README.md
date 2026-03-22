# Hangarin | Task Management System

**Hangarin** is a streamlined, Django-based web application designed to help users organize, track, and prioritize their daily tasks and professional goals. Built with a focus on simplicity and efficiency, it provides a structured way to manage complex workflows through categorized tasks and sub-tasks.

## Features

* **Task Management:** Create, update, and track tasks with dedicated status levels (Pending, In Progress, Completed).
* **Hierarchical Organization:** Group tasks by **Category** and assign **Priority** levels to focus on what matters most.
* **Sub-tasks & Notes:** Break down large goals into manageable steps and attach detailed notes to specific tasks.
* **Modern Admin Interface:** Powered by the **Django Unfold** theme for a professional, high-visibility dashboard.
* **Responsive Design:** Uses **Tabler CSS** to ensure the interface works smoothly across desktop and mobile devices.

## Tech Stack

* **Framework:** Django (Python)
* **Database:** SQLite (Development)
* **Frontend:** HTML5, Tabler CSS, JavaScript
* **Admin UI:** Django Unfold

## Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Daiyukisen/hangarin.git](https://github.com/Daiyukisen/hangarin.git)
   cd hangarin
2. **Install dependencies:**
   pip install -r requirements.txt
3. **Apply migrations:**
   python manage.py makemigrations
   python manage.py migrate
4. **Run the server:**
   python manage.py runserver

## 🌐 Deployment
This project is optimized for deployment on **PythonAnywhere**. 

### Deployment Checklist:
1. **Static Files:** Run `python manage.py collectstatic` to consolidate CSS/JS for production.
2. **Environment:** Ensure the virtual environment is active and all dependencies in `requirements.txt` are installed.
3. **Web Configuration:** Map the `/static/` URL to the generated `staticfiles` directory in the PythonAnywhere Web tab.
