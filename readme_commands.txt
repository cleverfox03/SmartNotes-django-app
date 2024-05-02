django-admin startproject <project_name> .  - to start a new project
django-admin startapp home  - to start a new app

python manage.py runserver  - to run the server

python manage.py migrate - syncing system and db

username - shiv
pass - cleverfox

Django uses ORM (Object Relational Mapping system) to handle db communications and changes
 - Add table structure as classes in models file
 - 'python manage.py makemigrations' to create migrations
 - 'python manage.py migrate' to apply changes to db 

 python manage.py shell - to open interactive shell to operate on db

 DB Query:
 from notes.models import Notes  - run this command first to tell shell that you are referring to the table

 <table_name>.objects.get(<condition>)  - used to get a db row based on condition given within (). condition example - pk='1' means primary key
 <table_name>.objects.all() - fetches all rows as objects
 <table_name>.objects.create(text='..', title='...')  - create a new row in db
 <table_name>.objects.filter(title__startswith='My')  - filter rows that have title starting with the value
 <table_name>.objects.filter(title__icontains='Django')  - filter rows that have title conatining the value
 <table_name>.objects.exclude(title__startswith='My')  - from whole db excludes rows that have title starting with the value
 <table_name>.objects.filter(title__startswith='My').exclude(title__icontains='Django')  - combined filter and exclude

4:
 Dymanic template is denoted by {% ___ %}
 eg:
 {% for note in notes %}
 --
 {% endfor %}

 views are created with classes instead of functions

5:
 static files such as css html are put in one folder in home
 html templates can be made with content block that can be filled by actual html pages
 use bootstarp for styling. include bootstrap link in base.html page and bootstrap methods can be called anywhere