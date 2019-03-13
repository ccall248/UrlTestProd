

# UrlTestProd

Django-based batch get and post tools.

# Introduce

The project consists of two parts: the front and the back: 

1. The back:<br>
	Based on the Django admin. <br>
	Used to define GET and POST requests.<br>
	You can choose to perform a get request or a post request separately, or both.<br>
2. The front:<br>
	Including two pages:<br>
	homepage.html--On this page, select which content to perform the dial-out.<br>
	summary.html--This page is used to display the dialing results, such as IP, response time,HTTP status code, and so on.<br>

# Requirement

python==3.6.5 <br>
certifi==2018.4.16 <br>
chardet==3.0.4 <br>
Django==2.0.5 <br>
idna==2.6 <br>
PyMySQL==0.8.1 <br>
pytz==2018.4 <br>
requests==2.18.4 <br>
urllib3==1.22 <br>

# How To Start UrlTestProd
  
```bash
$ nohup python manage.py runserver 125.210.162.45:8000 &
```

#Screeshot

![](http://s2.postimg.org/728c1wy4p/Screenshot_5.png)

![](http://s30.postimg.org/fflxcv9ld/Screenshot_6.png)
