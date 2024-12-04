# SCA ( Spy Cat Agency ) Management App

# Warning!

This project assumes that you will use any linux distro. <br>
The Owner not sure that it will work on Windows or MacOs. <br>
Highly recommended to use any Linux distro or at least Windows + WSL


# Setup
### 1. Clone the project
```bash
git clone https://github.com/GhostMEn20034/sca_management_app.git
```
### 2. Go to `sca_management_app` directory
```
cd sca_management_app
```
### 3. Create `.env` file, here's an example:
```
SECRET_KEY=django-secret-key ( you can generate Django secret key here: https://djecrety.ir/ )
JWT_SIGNING_KEY=some_jwt_secret_key ( you can generate JWT secret key here: https://jwtsecret.com/generate )
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000,http://localhost:3001,http://127.0.0.1:3001
SUPER_USER_PWD=postgres
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=sca_management
SQL_USER=sca_management_usr
SQL_PASSWORD=xxxx1111
SQL_HOST=db
SQL_PORT=5432
SQL_CONN_MAX_AGE=60
```
### 4. Change permissions for `init-database.sh`:
```bash
chmod +x init-database.sh
```
### 5. Run the server using command:
```bash
docker compose up -d --build
```

### 6. Execute the command to go inside of the Django container's file system:
```
docker exec -it sca_web /bin/bash
```

### 7. Run the command below and fill all required data to create user:
```
python manage.py create superuser
```
### 8. Go to [localhost:8000](http://localhost:8000) and test your server using tools such as Postman

# Remove mandatory authentication
### 1. If you don't want to have required authentication, you can go to `sca_management_app` directory using command:
```bash
cd sca_management_app
```
### 2. Open `settings.py` file
### 3. Change this line ( Line # 130) from:
```
'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
```

to:
```
'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
```


# Postman Collection Link:
https://elements.getpostman.com/redirect?entityId=24907978-0afc7b74-faed-464e-8507-a885e0562886&entityType=collection

<br>

All Routes require an Authentication. <b>Set Header "Authorization" to "Bearer your_jwt_token" in each request</b>
