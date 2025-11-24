# Fraud Detection for Multi-Participant E-commerce Systems

A machine learning–based fraud detection system designed for **multi-participant e-commerce platforms**.
This project analyzes user behavior, transaction patterns, interaction signals, and content features to identify fraudulent activity.
It provides role-based interfaces for remote users and service providers, includes dataset upload tools, model training modules, and fraud ratio visualizations.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Backend Setup](#backend-setup)
- [Using the Application](#Using the Application)
- [Dataset](#Dataset)
- [Developer](#Developer)

 ---

## Overview

**Fraud Detection for Multi-Participant E-commerce Systems** is designed to detect fraudulent activity across complex e-commerce environments where multiple users interact.
The system uses machine learning models to classify user activity as legitimate or fraudulent based on behavioral and transactional features.

Backend interactions are powered by **Django**, combined with structured datasets and trained ML models.
The frontend includes user and admin panels built with **HTML, CSS, and Django templates**.

---

## Features

- Machine learning and deep learning models for fraud detection
- Multi-participant user behavior and interaction analysis
- Remote User and Service Provider role-based access
- Dataset upload and model training interface
- Real-time fraud prediction for remote users
- Fraud ratio visualization for service providers
- SQL database integration for storing users and activity logs
- Template-driven user interface
- Complete Django-based backend architecture

---

## Tech Stack

**Backend**

Python

Django Framework

SQLite / SQL

**Machine Learning**

Pandas

NumPy

Scikit-learn

Matplotlib

**Frontend**

HTML

CSS

**Tools**

pip

Virtual Environment (venv)

---

## Project Structure

Fraud Detection for Multi-Participant E-commerce Systems
│
├── a_multiperspective_fraud_detection/
│ ├── Remote_User/
│ ├── Service_Provider/
│ ├── Template/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── manage.py
│
├── Database/
│ └── a_multiperspective_fraud_detection.sql
│
├── Datastructure.txt
└── README.md

---

## Backend Setup
## 1. Navigate to the project directory
cd A_Multiperspective_Fraud_Detection

## 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # On Windows
source venv/bin/activate     # On Linux/Mac

## 3. Install dependencies

(If requirements.txt is needed, I can generate one.)

pip install django pandas numpy scikit-learn matplotlib

## 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

## 5. Start the development server
python manage.py runserver


Your backend will run at:
http://127.0.0.1:8000/

Using the Application

---

## Remote User

Register and log in

Submit fraud detection inputs

View prediction results

---

## Service Provider

View fraud detection ratios

Manage datasets

Train the machine learning model

View user activity status

----

## Dataset

This project uses custom datasets included in the repository such as:

Datasets.csv

Results.csv

These datasets are used for training, evaluating, and predicting fraud.

---

## Developer

Jayanth Sadurla
B.Tech CSE (Data Science), Class of 2026
Focused on building AI/ML-powered intelligent applications and scalable backend systems.
