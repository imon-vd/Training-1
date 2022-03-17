# Forms with Django 📃
## Form manipulation and Sending Email with Django.

Hi! Our team at Vakildesk Welcomes you to our first training session. We will be teaching you how to build a form with Django. This will give you a bit of sense of how we work at <b>Vakildesk</b> and get you upto speed.

You will be given a boilerplate project which is partially complete , and rest you have to figure out accroding to the requirements.

    PS: This project assumes you have PostgreSQL server installed and running in your computer.
## By the end of this you'll know how to :
1. Handling Form Submissions.
2. Validating Form Fields.
3. Saving Form Entries in DataBase.
4. Serving a File.
5. Sending emails using Django.

# Setting up the project.

- Open up a terminal .

- To set up the project , first clone this repository in your local.

        git clone https://github.com/imon-vd/Training-1.git
- CD into the directory.

        cd Training-1(or whatever the name of the folder is)

- Add Static Files: To get static files, please go to releases and download static.zip file.
    - extract static.zip file, you'll get a static named folder.

    - Add this to `Project Root` ie inside the `Training-1` folder.


- Add .env File : Add an env file in `forms_with_django` directory for environment variables.

    You can do so by just creating a file with no name and an extension : .env .
    The variables you may need to add would be discussed in the next section.


- Create a virtualenv.
        
        python3 -m venv venv # For Linux
        python -m venv venv # For Windows
- Activate the virtualenv.
        
        source venv/bin/activate # For Linux
        .venv/scripts/activate # For windows
- Install dependencies.
        
        pip install -r requirements.txt
    This should install all the dependencies needed for running this project.

- Connect Postgres.

    At VakilDesk we use [PostgreSQL](https://www.postgresql.org/). This tutorial assumes you have already setup postgresql and have created a new server to connect it to the project.

    To enable postgreSQL you have to pass in the connection details to the settings file , by adding key value pairs to the .env file that you created earlier.
    
    `Keys Required:`
    
    - `DB_NAME` Name of the database you created and will connect to and store data while using this project.
    - `DB_USER` Name of the user that has access to the database. Please create a user before setting this if not already done so.
    - `DB_PASSWORD` Password for the username password pair to connect to the database.
    - `DB_HOST` Hostname of the server that the database is running on.


- Make migrations and run the project.

        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver localhost:8000


Your server should now be running.

# Info about the Project.
So , this is a basic project.

You're a backend developer at Vakildesk. Our client needs a form so that he can get the information about his customers.

A Customer wants to give his personal data to the client cause they trust the client wholeheartedly.

These include :
- Name.
- Phone Number.
- Email.
- City.
- State.
- Country.
- Zip Code/ PIN Code.
- A File containing their Resume/ CV. [PDF]

Anyone can add their data using your app.
But only the admin can view the data.

Your task is to finish the incomplete app and build according to the Requirements.

# Routes:

```/ [GET , POST]```:

Home Page. Contains the form.

- on ```GET```  should return the homepage.

- on ```POST``` Should take in te data, store it in the database, and send the user an email thanking them for giving us all their information. After sending the email , we should be returning a ```thank you``` page thanking them for using our service.

###
    PS: You should add this to the userdata module.

```/Admin [GET , POST, UPDATE, DELETE]```:

If you know ```Django``` , you will know Django makes life a lot easier for developers.
And that includes a inbuilt ```admin panel```.
But why an admin panel? How does it help us?
Well admin panel lets us view the database and its entries , and add modify and delete data without needing to use SQL / some viewer. 

 In production it can also help the site manager to supervise and carry out different tasks using it. You can learn more about Django Admin panel and its capabilities [here](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/).

But no need to worry. We won't be doing much right now. All we have to is 

Let the client go to the admin panel , and he should be able to see all the entries of his customers.

In addition to that he should be able to:
- Filter according to :
    - date of entry.📅
    - state. 🏠
    - country.🚩
    - city. 🏙
- Sort according to :
    - date of entry. 📅
- Search by 🔎:
    - Name. 📝
    - Email. 📧
    - Phone Number. 📞

###
    PS: You should add this to the userdata module.
# Let's start with what you have to do then?

## Your Tasks:
- Let's start with the ```form```. The form is located under templates/userdata/form.html.
It currently has the following fields:
    - Name. `required`
    - Email. `required`
    - City. `optional`
    - State. `optional`
    - Country. `optional`
    - Zip Code/ PIN Code. `optional`
    - A File containing their Resume/ CV. [PDF] `optional`
    
    Add the missing fields to the form.
    Make sure to follow the design.

- In order to properly handle the form , we need a model to store the data. Django takes care of this by giving us an` ORM`. An ORM is a nifty piece of code taht lets us use databases without having to write tedius Amount of SQL codes. Instead it can be done in a pythonic way. It supports multiple different databases and hence makes it easier to shift to different databases. Read more about it [here](https://docs.djangoproject.com/en/4.0/topics/db/models/).

   With the ORM we get a models.Model class that we can use to build and register our own models(tables in SQL lingo).

   According to Django's design pattern and our design pattern too , we would be saving all the models required to be created for a module/app in the app's `models.py` file. 

   On opening `userdata/models.py` you'll see that there is one model with a name UserData.

   Read through the comments and add the *missing model fields* and create migrations and migrate the database. If you run into issues try to google it. No shame in `googling`, we all do that ;).

        PS: For saving the file , you should use FileField(). Keep it null=True , blank=True cause the file is a optional input. Follow django's documentation for handling the file.

- Let's move to the admin field now. As discussed above , the admin panel is a part of Django. And the client needs the admin panel.

    Move to `userdata\admin.py` and you'll see that there is an empty class called `UserDataAdmin`. Add requirements to the class to extend the admin panel to show different field filters and search options.

        Hint: use tuples:
        - list_filter = ()
        - search_fields = ()
        - list_display = ()
        to add filter and search options.

- Let's handle the backend too. The form is served by a function called `formdata` in `userdata.views`.

    The function currently serves the page on get request. We want to handle the post call and store the data in the database too. Go through the function and add the requirements.


Once all the requirements are done. Try the project out. Make changes , increase functionality and see how it works.

## Congratulations!🥳
### You've learned how to handle forms in Django.

# Going Above and Beyond
## Sending Email using Django.📧
At this point , you have a working Django application that can take in user details.
Why not we send an email to the user letting them know how much we care about them.

For that we would need to add emails.
Don't worry though , you won't have to write your own email sender . Django does it for you!
Go to `settings.py` in the main project directory , ie `forms_with_django` , you will see there's a line called : `# Email Configuration`

Follow the link to learn how to set up emailing in django.

Once Done Come back to `userdata/views.py`
 and in the elif part of the code add logic to handle sending email .

 - Import the `send_mail` function from the `django.core.mail` module. Also import `settings` from the `django.conf` module to access the email configuration.

 - `send_mail` takes in different values ,
    configure it so that , user should get an email to their given email address with a 
    - `subject` : Welcome to the Test.
    - `body` : thank you for giving your data.
    Follow [Django's Documentation](https://docs.djangoproject.com/en/4.0/topics/email/) for understanding how to setup Emails.



#
# Congratulations!🎉🥳
You have learnt how to :
- Handle forms in Django. ✅
- Handle models in Django.✅
- Handle sending emails in Django.✅
- Customise the admin Panel to your liking.✅

Until Next time! 



