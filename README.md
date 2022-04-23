## HACKER NEWS API
***

### Instructions

The goal is to make a web app to make it easier to navigate the news:

- Choose a web framework of your choice. Django, Flask, use what you like. Make a new virtualenv and pip install it;
- Make a scheduled job to sync the published news to a DB every 5 minutes. You can start with the latest 100 items, and sync every new item from there. Note: here are several types of news (items), with relations between them;
- Implement a view to list the latest news;
- Allow filtering by the type of item;
- Implement a search box for filtering by text;
- As there are hundreds of news you probably want to use pagination or lazy loading when you display them.
It is also important to expose an API so that our data can be consumed:

- GET : List the items, allowing filters to be specified;
- POST : Add new items to the database (not present in Hacker News)

### Steps to run this code.

- To start this code a virtual environment has to be created.
- install dependencies using `$ pip install -r requirements.txt`.
- To start the api fetching process run `$ python News_api.py`.
- Then run the django project using `$ python manage.py runserver`