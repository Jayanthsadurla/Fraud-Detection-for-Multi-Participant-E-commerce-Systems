# Fraud Detection for Multi-Participant E-commerce Systems

A multi-perspective fraud detection web application designed to detect and analyze fraudulent transactions in platforms with multiple participants (remote users, service providers). Built with Django, Python ML tools and web UI modules.

---

## Table of Contents  
- Overview  
- Features  
- Tech Stack  
- Project Structure  
- Setup Instructions  
- Usage  
- Developer  
- License  

---

## Overview  
This project addresses fraud detection in e-commerce scenarios involving multiple types of users. It uses machine learning models and rule-based logic to identify suspicious behaviours from both remote users and service providers. The platform supports dataset uploads, model training and visual result dashboards.

---

## Features  
- User modules for Remote Users and Service Providers.  
- Dataset upload & model training workflows.  
- Visualizations of fraud detection metrics (charts, status, ratios).  
- Downloadable trained models and result reports.  
- Dashboard showing detection results and user status.  

---

## Tech Stack  
**Backend & ML:**  
- Python  
- Django  
- Machine Learning (Pandas, Matplotlib, Scikit-learn, etc.)  

**Frontend & UI:**  
- HTML / CSS templates  
- Django templates (for Remote User / Service Provider)  

**Development Environment:**  
- SQLite or local database  
- Virtual environment setup (venv)  

---

## Project Structure  
Fraud-Detection-for-Multi-Participant-E-commerce-Systems/
├── manage.py
├── Database/
├── Datasets/
├── Service_Provider/
│ ├── models.py
│ ├── views.py
│ └── …
├── Remote_User/
├── Template/
│ ├── RUser/
│ └── SProvider/
├── media/
├── requirements.txt
└── venv/ (optional, not included in repo)

--
## 1. Clone the repository
git clone https://github.com/Jayanthsadurla/Fraud-Detection-for-Multi-Participant-E-commerce-Systems.git  
cd Fraud-Detection-for-Multi-Participant-E-commerce-Systems
## 2. Create and activate a Python virtual environment
python -m venv venv  
venv\Scripts\activate      # On Windows  

source venv/bin/activate   # On Linux/Mac
## 3. Install dependencies
pip install -r requirements.txt
## 4. Run database migrations
python manage.py migrate
## 5. Start the development server
python manage.py runserver

---
## Usage

Navigate to the web application in your browser (default: http://127.0.0.1:8000/).

Upload datasets and initiate training workflows.

Explore the dashboards under Remote User / Service Provider modules to view fraud detection results.

Download trained models and result summaries as needed.

---

## Developer

Jayanth Sadurla
B.Tech CSE (Data Science), Class of 2026
Focused on developing AI/ML driven full-stack applications to solve real-world problems.


