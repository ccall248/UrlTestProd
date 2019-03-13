

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

# Examples

The Backstage Pages: <br>

![](https://github.com/ccall248/UrlTestProd/blob/master/pagetest/static/images/backstage.png) <br>
![](https://github.com/ccall248/UrlTestProd/blob/master/pagetest/static/images/backstage_get.png) <br>
![](https://github.com/ccall248/UrlTestProd/blob/master/pagetest/static/images/backstage_post.png) <br>
![](https://github.com/ccall248/UrlTestProd/blob/master/pagetest/static/images/backstage_area.png) <br>

The Front Pages: <br>

![](https://github.com/ccall248/UrlTestProd/blob/master/pagetest/static/images/front_choose.png) <br>
![](https://github.com/ccall248/UrlTestProd/blob/master/pagetest/static/images/front_result.png) <br>
