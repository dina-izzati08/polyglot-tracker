# Polyglot Tracker

A full-stack learning tracker built to practice multiple technologies simultaneously.

## Tech Stack
- **Django** — REST API backend
- **Python (pandas, matplotlib)** — data science and visualisation
- **Java** — API client and data processing

## Features
- Log study sessions by topic, language and minutes
- REST API endpoint at `/api/entries/`
- Data science analysis with charts
- Java client that consumes the Django API

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API
`GET http://127.0.0.1:8000/api/entries/` — returns all learning entries as JSON