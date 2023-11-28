# Vendor
Vendor Management System with Performance Metrics

# Prerequisite
- python
- postgres
- pip

# Setting up the project

setup database (postgres cli):
```
CREATE DATABASE Vendor;
CREATE USER admin WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE Vendor TO admin;
ALTER USER admin CREATEDB;
```

setup python environment:
```
python -m venv venv
source venv/bin/activate
cd vendor
pip install -r requirement.txt
```

migrating the database:
```
./manage.py makemigrations
./manage.py migrate
```

create a superuser:
```
./manage.py createsuperuser
```

# Running Test
```
./manage.py test
```

# Starting surver
```
./manage.py runserver
```

Note:<br>
Admin panel: ```127.0.0.1:8000/admin/```<br>
API documentation url (swagger): ```127.0.0.1:8000/swagger/```<br>
API documentation url (redoc): ```127.0.0.1:8000/redoc/```



