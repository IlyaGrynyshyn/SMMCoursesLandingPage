# SMMCoursesLandingPage

This site was developed to sell SMM courses. It has 2 pages, the first page contains all the information about the course, the second page is for signing up for the course

## Figma prototype
   You can check out the template in figma -> [click](https://www.figma.com/proto/jX2f9VqYcyMZuZRRpHh5ju/SMM%26Psychology?node-id=8-21472) 

## Technologies Used

- Django
- HTML/CSS/JavaScript
- Database

## Usage Instructions

Ensure that Python is already installed on your machine.

1. Installation:
   - Clone the repository: git clone https://github.com/yourusername/smm-courses-hub.git.
   - Create a virtual environment: python3 -m venv venv.
   - Install dependencies: pip install -r requirements.txt.

2. Running:
   - Apply migrations: `python manage.py migrate` 
   - Start the server: `python manage.py runserver`
   - Access the platform: http://localhost:8000 in your web browser.

## Developer Commands

- python manage.py makemigrations: Create database migrations.
- python manage.py migrate: Apply migrations to the database.
- python manage.py createsuperuser: Create a site administrator.
