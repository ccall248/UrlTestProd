

# UrlTestProd

Django-based batch get and post tools.

# Introduce

The project consists of two parts: the front and the back: 

1. The back:
	Based on the Django admin. 
	Used to define GET and POST requests.
	You can choose to perform a get request or a post request separately, or both.
2. The front:
	Including two pages:
	homepage.html--On this page, select which content to perform the dial-out.
	summary.html--This page is used to display the dialing results, such as IP, response time,HTTP status code, and so on.

# Requirement

python==3.6.5
certifi==2018.4.16
chardet==3.0.4
Django==2.0.5
idna==2.6
PyMySQL==0.8.1
pytz==2018.4
requests==2.18.4
urllib3==1.22

# How To Start UrlTestProd
  
```bash
$ nohup python manage.py runserver 125.210.162.45:8000 &
```

#Screeshot

![](http://s2.postimg.org/728c1wy4p/Screenshot_5.png)

![](http://s30.postimg.org/fflxcv9ld/Screenshot_6.png)
