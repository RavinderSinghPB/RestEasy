# Foodkart

>## Features

- ### customer, Login to the application
- ### customer can view list of Food vendors
- ### customer,  view the dishes
- ### customer, add items and quantity to cart
- ### customer, can order many dishes along with quantity 
- ### Order Item can be from different vendor 
- ### Dish can be sold by different vendor with different price, only name and calories same
- ### vendor can view all the orders
- ### customer, can order many dishes along with quantity 
- ### Order Item can be from different vendor 
  

## Packages Used 

- Django 
- Django_rest_framework

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/RavinderSinghPB/RestEasy.git
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv -p python3 foodkart
$ source foodkart/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv foodkart
$ # .\foodkart\Scripts\activate
$
$ # go to project directory
$ cd RestEasy
$ 
$ # Install required packages/modules 
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```
