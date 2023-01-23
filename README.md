# Rabbit Like Checker

A simple project which posts created at the Posts project are passed as messages using RabbitMQ and appropiate operations done on them at the receiving end, the Likes project.

## Installation guide, step by step:
First of all, clone the project:
```
git clone https://github.com/EngRobot33/Rabbit-Like-Checker.git
```
Then, we need a virtual environment. You can create like this:
```
virtualenv venv
```
Activate it with the command below:
```
source venv/bin/activate
```
After that, you must install all of the packages in `requirements.txt` file in project directory:
```
pip install -r requirements.txt
```

For running the project, follow the instructions below:

**Posts project**
```
cd Posts
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 consumer.py
```
**Likes project**
```
cd Likes
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 consumer.py
```
**Communication**

First, make sure you have installed [RabbitMQ](https://www.rabbitmq.com/install-debian.html) and [pika](https://pypi.org/project/pika/).

If you are a linux user, run the RabbitMQ server:
```
sudo service rabbitmq-server start
```
Else, follow the instructions for [Windows](https://www.rabbitmq.com/install-windows-manual.html) and [Mac](https://www.rabbitmq.com/install-homebrew.html).

Finally, create, edit or delete posts on Posts project and similar opertaions happen at the Likes project.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
