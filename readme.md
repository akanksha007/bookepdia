Webapp using django framework.
Webapp displays multiple image on home page, of multiple items. 
Hovering on image displays item's name. 
Clicking on each image opens a webpage with brief description of the content related to item.

Assuming you have django installed, follow these steps to run the app.

git clone git://github.com/akanksha/bookepdia.git
cd bookepdia

Now we need to create the database tables . On Django 1.6 and below, run the following command.

$ python manage.py syncdb --migrate

On Django 1.7 and above:

$ python manage.py migrate

Now you need to run the Django development server:

$ python manage.py runserver

You should then be able to open your browser on http://127.0.0.1:8000 .

