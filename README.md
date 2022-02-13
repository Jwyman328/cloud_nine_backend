To start the project run without docker 

## create a virtual enviornment
$ virtualenv -p python3 virtual_env_cloud_nine_backend

## start virtual env 
$ source virtual_env_cloud_nine_backend/bin/activate

##install all requirements 
$ pip install -r requirements.txt
##may need to do pip3 install

#set up the database
$ python manage.py makemigrations
$ python manage.py migrate

#start up server on port 8000
$ python manage.py runserver 0.0.0.0:8000


To start the project with docker 
$ docker-compose up