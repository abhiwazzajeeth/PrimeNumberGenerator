# Homework_1
#### Prime Generator
The prime generator web app is implemented in Python using the Django Framework.
This webapp takes a positive integer, and generates prime numbers until that integer.
The user provides a postive integer. The code runs on the server and gives the prime numbers until that number.
The prime numbers are generated using the 'Sieve of Eratosthenes' for prime generation.
The app is live at http://3.16.186.199

##### Deploying web app on AWS EC2 instance using Nginx.

sudo apt install $(cat requirements)
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
Activate virtual environment
pip install django
Git clone the project.
sudo ufw allow 8000

#### add below at /etc/systemd/system/gunicorn.socket

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target

#### add below at /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=username
Group=www-data
WorkingDirectory=/home/username/projectdir
ExecStart=/home/username/projectdir/projectenv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          projectname.wsgi:application

[Install]
WantedBy=multi-user.target

#### add below at /etc/nginx/sites-available/project

server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/username/projectdir;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}


#### References :
1. https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#checking-for-the-gunicorn-socket-file
2. https://docs.djangoproject.com/en/1.10/intro/tutorial01/  (tutorial building an application in Django)
3.http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html (setting up Django to deploy
