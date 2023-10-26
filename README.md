# The Dining Place #

[Click here to visit the live page.](https://the-dining-place-242cd25ddaad.herokuapp.com/)

[Click here to visit the Github repository.](https://github.com/TamasSomi/the-dining-place)

![Responsive screenshot of the home page.](/static/docs/home-page.png)


This page is a fictive restaurants page with registration and booking options. It was built with learning purposes.


## User stories ##

[Click here to read the user stories on Github Issues](https://github.com/TamasSomi/the-dining-place/issues)


## Target Audiance ##

* People who enjoy going out for food and interested in gastronomy.

* They prefer to book a table insted going with not having a booked table.

* People who prefer booking online instead of calling the restaurant.


## Features ##
(More screenshots of the app present in the Testing section)

* User can register.

* User can see the menu and the restaurent's details.

* User can book a table online and see all the already existing bookings.

* User can update or delete the booking.

* User can not book a table twice for the same time.
![Screenshot of double booking validation](/static/docs/double-booking-screenshot.png)

* The booking form is validated, so the user can not book a table with any invalid data.
![Screenshot of invalid input validation](/static/docs/invalid-data.png)


## Future Features ##

* Fast login with Facebook or Google.

* Email sent with the details after booking a table.

* Edit button will not show on expired bookings.


## Planning ##

 The data model will define a 'Booking' class with the following fields:

 * 'user': A foreign key to the user model, representing the user who made the booking.

 * 'name': A character field for the name of the person who made the booking.

 * 'email': An email field for the contact email for the person who made the booking.

 * 'phone_number': A character field for the contact phone number.

 * 'date_time': A datetime field that represents the date and time for the booking.

 * 'pax': A positive integer field that represents the number of people for the booking.

 * 'comments': A text field for any additional information, notes related to th booking.


## Technology Used ##

Used technologies during development:

* [Github](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Heroku](https://dashboard.heroku.com/)
* [Django](https://www.djangoproject.com/)
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/#)
* [Django Allauth](https://docs.allauth.org/en/latest/#)
* [Whitenoise](https://whitenoise.readthedocs.io/en/latest/#)
* [Bootstrap](https://getbootstrap.com/)
* [ElephantSql](https://www.elephantsql.com/)


## Manual Test ##

|      Test Case       |         Steps         |           Expected Results            |   Result   |
| ------------------ | --------------------- | ------------------------------------- | ---------- |
| Registration       | 1. Navigate to the   | 1. The registration page is displayed. |   1. Pass.  |
|                    | registration page.   | 2. All fields accept valid input.     |   2. Pass.  |
|                    | 2. Fill in all      | 3. The user is redirected to the      |   3. Pass.  |
|                    | required fields     |    dashboard.                        |            |
|                    | with valid data.     |                                        |            |
|                    | 3. Click the         |                                        |            |
|                    | register button.     |                                        |            |
| ------------------ | --------------------- | ------------------------------------- | ---------- |
| Login              | 1. When logged out,  | 1. The login page is displayed.       |   1. Pass.  |
|                    | click on the Login   | 2. All fields accept valid input.     |   2. Pass.  |
|                    | button.              | 3. The user is redirected to the     |   3. Pass.  |
|                    | 2. Fill in the fields|    dashboard.                        |            |
|                    | with an existing    |                                        |            |
|                    | user name and        |                                        |            |
|                    | password.            |                                        |            |
|                    | 3. Press the Sign in |                                        |            |
|                    | button.              |                                        |            |
| ------------------ | --------------------- | ------------------------------------- | ---------- |
| Logout             | 1. When logged in,   | 1. The login page is displayed.       |   1. Pass.  |
|                    | click on the Logout  | 2. User redirected to the home page.  |   2. Pass.  |
|                    | button.              |                                        |            |
|                    | 2. On the logout page|                                        |            |
|                    | click on the Sign    |                                        |            |
|                    | Out button.          |                                        |            |
| ------------------ | --------------------- | ------------------------------------- | ---------- |
| Booking a table    | 1. Go to the          | 1. Under the hero image, a form       |   1. Pass.  |
|                    | dashboard by clicking |    displayed with fields of name,    |   2. Pass.  |
|                    | on the Bookings       |    email, phone number, date-time,  |   3. Pass.  |
|                    | button.              |    pax, and comments.                |            |
|                    | 2. Fill the booking   | 2. The form accepts only valid data.  |            |
|                    | form with valid data.|    All fields required but the       |            |
|                    | 3. Press the submit  |    comments field.                   |            |
|                    | button.              | 3. The user is redirected to the     |            |
|                    |                     |    booking success page.             |            |
| ------------------ | --------------------- | ------------------------------------- | ---------- |
| Edit a booking     | 1. Go to the          | 1. The booking cards are displayed   |   1. Pass.  |
|                    | dashboard by clicking |    under the My Bookings title.      |   2. Pass.  |
|                    | on the Bookings       | 2. The user is redirected to the     |   3. Pass.  |
|                    | button.              |    edit_booking page.                 |   4. Pass.  |
|                    | 2. Click edit on one  | 3. The user is able to change the    |            |
|                    | of your bookings.     |    desired field with valid data.    |            |
|                    | 3. Change the data.   | 4. The user is redirected to the     |            |
|                    | 4. Press the save     |    dashboard, the card displayed     |            |
|                    | changes button.      |    with the updated data.            |            |
| ------------------ | --------------------- | ------------------------------------- | ---------- |
| Delete a booking   | 1. Go to the          | 1. The booking cards are displayed   |   1. Pass.  |
|                    | dashboard by clicking |    under the My Bookings title.      |   2. Pass.  |
|                    | on the Bookings       | 2. The user is redirected to the     |   3. Pass.  |
|                    | button.              |    delete_booking page.              |            |
|                    | 2. Click delete on   | 3. The user is redirected to the     |            |
|                    | one of your bookings. |    dashboard. The deleted booking    |            |
|                    | 3. Click on the      |    is not displayed anymore.         |            |
|                    | Confirm Delete button.|                                      |            |
| ------------------ | --------------------- | ------------------------------------- | ---------- |
| Responsiveness Test| 1. Acces the website  | 1. The website is fully displayed with| 1. Pass.    |
|                    | with a desktop computer.| all content and features accessible | 2. Pass.    |
|                    | Open up the devtool and | and usable.                        |               |
|                    | set all the available |  2. All elements function as expected|               |
|                    | devices.                 | on both desktop and mobile versions.|             |
|                    | 2. Verify that all content|                                     |            |
|                    | and features are properly |                                     |            |
|                    | displayed and usable on all|                                     |           |
|                    | devices.                    |                                    |           |
| ------------------ | --------------------- | ------------------------------------- | ---------- |
| Reading an existing booking | 1. Go to the dashboard by   | 1. The already existing | 1. Pass. |
|                             | clicking on the Bookings button.| bookings are displayed|         |
|                             |                              | under the Bookings title with|     |
|                             |                          | all the necessary data. |               |
| ------------------ | --------------------- | ------------------------------------- | ---------- |


* Responsive screenshot of the home page.
![Responsive screenshot of the home page.](/static/docs/home-page.png)

* Responsive screenshot of the login page.
![Responsive screenshot of the login page.](/static/docs/signin-page.png)

* Responsive screenshot of the register page.
![Responsive screenshot of the register page.](/static/docs/register-page.png)

* Screenshot of the booking form.
![Screenshot of the booking form.](/static/docs/booking-form.png)

* Screenshot of the booking cards.
![Screenshot of the booking cards.](/static/docs/booking-cards.png)

* Screenshot of the edit booking page.
![Screenshot of the edit booking page.](/static/docs/edit-booking.png)

* Screenshot of the delete booking page.
![Screenshot of the delete booking page.](/static/docs/delete-booking.png)

## Validator Testing ##

* Screenshot of the Python Linter test (views.py).
![Screenshot of the Python Linter test (views.py).](/static/docs/view-python-linter-test.png)

* Screenshot of the Python Linter test (models.py).
![Screenshot of the Python Linter test (models.py).](/static/docs/model-python-linter-test.png)

* Screenshot of the Python Linter test (forms.py).
![Screenshot of the Python Linter test (forms.py).](/static/docs/forms-python-linter-test.png)

* Lighthouse Test
![Lighthouse test result screenshot](/static/docs/lighthouse-testresult.png)

For some reason Lighthouse couldn't make screenshots during the tests which caused an error for performance test. 
![Lighthouse test error screenshot](/static/docs/lighthouse-error.png)

## Security Features ##

* User is authenticated and can not edit any booking without logging in.
* Just the user created the booking can access and manipulate existing bookings.
* A user can not see other user's details and bookings.

## Bugs ##

### User could book a table twice for the same date and time. ###

- Solved by creating the clean function that checks if there is an existing booking with the user's
and the date and time and raises a ValidationError.

### User could book a table for less then one person. ###

- Solved by creating the validate_pax function which checks the value of the field and raises a ValidationError if needed.

### User could book a table in the passt. ###

- Solved by creating the validate_datetime function which checks if the time now is less than the time for the booking and raises an error if needed.

## Deployment ##

### This website was deployed to Heroku and developed using Github and Gitpod ###

* Steps for deployment:

* Open the repository of the page. You can find the link in the readme.md.
* To clone or fork the repo, click on the Gitpod (or any IDE you have installed) button.
* Create your own repository and use git add . git commit -m "..." and git push commands.
* Create a new app on Heroku.
* Click on your app's name to enter the app dashboard.
* Go to the "Deploy" tab.
* In the "Deployment method" section, choose "GitHub."
* Click the "Connect to GitHub" button.
* Follow the prompts to authorize Heroku to access your GitHub account.
* Search for and select your GitHub repository.


## Credit ##

* Code Institute "I Think therefor I blog" walkthrough project helped me a lot with setting up the project and using Django.
* Code Institute's Bootstrap tutorials were a big help with designing the page effectively.
* [The Code Insitute Github Agile Tool video](https://www.youtube.com/watch?v=U_dMihBgUNY)
* [Stackoverflow for calendar widget.](https://the-dining-place-242cd25ddaad.herokuapp.com/)
* [Using primary key.](https://iqcode.com/code/python/pk-django)
* [For django model form](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/)
* [Istock for the stock image](https://www.istockphoto.com/)
* [Font Awsome icons](https://fontawesome.com/icons)
* [Validating the form](https://docs.djangoproject.com/en/4.2/ref/forms/validation/)
* [Django hidden input field](http://www.semicolom.com/blog/add-a-hidden-field-to-a-django-form/)
* [Django input field initial value](https://stackoverflow.com/questions/604266/django-set-default-form-values)