# Credit-Approval-system

## Table of Contents

- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Technology Used](#technology-used)


## Getting Started
- Clone the repository, run  `git clone https://github.com/Srijan-SS02/Credit-Approval-System.git`
- Then create a virtual env `virtualenv venv`
- Now activate it `source venv/bin/activate`

  ## Configuration
- Install all the dependencies by running `pip install -r requirements.txt`

  ## Database Setup
- setup an .env file
- and enter the data according to .env.example file
- run celery by the command `celery -A credit_approval_system worker -l info`
- on another terminal with venv activate run following:-
- `python3 manage.py shell`
- `from credit_app.tasks import import_customer_data, import_loan_data`
- `import_customer_data.delay()`
-  check the response status in terminal where you have run celery, if positive move ahead with another injestion
- `import_loan_data.delay()`

  ## Running Application 
- You can run the data either by doing `docker compose up`
- or by manually running `python manage.py runserver`

  ## Technology Used
  - Django
  - REST
  - PostgreSQL
  - DOCKER  / Docker-compose
  - GithubAction
  - Celery
  - Rabitmq(message broker)
  - DockerHub
  - git
  
