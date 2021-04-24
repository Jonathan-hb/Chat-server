# Introduktion
This is the backend/server side of my message app. 

# Installation

To install your own backend of the app simply run these commands in linux:

Firstly install python3 and pip3

```
sudo apt install python3 python3-pip
```

Then install git:

```
sudo apt install git
```

Then you have to clone the repo with all the code:

```
git clone https://github.com/Jonathan-hb/Chat-server.git
```

Cd into the new folder with all the code

```
cd Chat-server
```

Then you have to install the python dependencies:

```
pip3 install -r requirements.txt
```

# Setup

Now you have all the code, but the server isnt running. 

First you have to make the database where all the data is going to be:

```
python3 manage.py migrate
```

Then create a superuser so you can login to the server as admin

```
python3 manage.py createsuperuser
```

Now fill in the infomation.

After you have created a superuser run the server:

```
python3 manage.py runserver
```

If there is no failiure then you can now acsess the site by going to the link: 127.0.0.1:8000/admin
If you sucsessfully are on the page login with the user you just made

Done, the server is up. 

# connect app to own private server

WARN: THIS IS NOT A FEATURE YET!

You can use your own server to make a private version of the app. If 