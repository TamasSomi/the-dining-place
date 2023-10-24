# The Dining Place #

[Click here to visit the live page.](https://the-dining-place-242cd25ddaad.herokuapp.com/)


This page is a fictive restaurants page with registration and booking options. It was built with learning purposes.


## User stories ##

[Click here to read the user stories on Github Issues](https://github.com/TamasSomi/the-dining-place/issues)


## Target Audiance ##

* People who enjoy going out for food and interested in gastronomy.

* They prefer to book a table insted going with not having a booked table.

* People who prefer booking online instead of calling the restaurant.


## Features ##

* User can register.

* User can see the menu and the restaurent's details.

* User can book a table online and see all the already existing bookings.

* User can update or delete the booking.

* User can not book a table twice for the same time.

* The booking form is validated, so the user can not book a table with any invalid data.


## Future Features ##

* Fast login with Facebook or Google.

* Email sent with the details after booking a table.


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


## Manual Test ##

| Summary          | Steps                    | Expected Results       | Result                 |
| --------------- | ------------------------- | ---------------------- | --------------------|
|  Registration     | 1. Navigate to the        |1. The registration page is displayed. | 1. Pass.  |
|                   | registration page.        |2. All fields accept valid input.      | 2. Pass.  |
|                   | 2. Fill in all required.  |3. The user is redirected to the dashboard.| 3. Pass.|
|                   | fields with valid data.    |                       |                      |
|                   | 3. Click the register button.                   |                           |
| --------------- | ------------------------- | ---------------------- | --------------------|
|  Login       | 1. When logged out, click  | 1. The login page is displayed. | 1. Pass.|
|                 |       on the Login button.   | 2. All fields accept valid input.| 2.Pass.|
|                   |  2. Fill in the fields with | 3. The user is redirected to  |  3. Pass. |
 |                   |    an existing user name   | the dashboard.                  |
  |                  |    and password.           |
 |                   |  3. Press the Sign in button.|
| --------------- | ------------------------- | ---------------------- | --------------------|
|  Logout           | 1. When logged in, click  | 1. The login page is displayed. | 1. Pass.|
|                 |       on the Logout button.   | 2. User redirected to the home page .| 2. Pass.|
|                   |  2. On the logout page |                                          |   |
 |                   |   click on the Sign Out button. |                  |                     
| --------------- | ------------------------- | ---------------------- | --------------------|
| Booking a table  | 1. Go to the dashboard by      | 1. Under the hero image   |   1. Pass.          |
|                  | clicking on the Bookings button| a form displayed with fields| 2. Pass.       |
|                  | 2. Fill the booking form with | of name, email, phone number,| 3. Pass.
|                  | valid data.                    | date-time, pax, and comments.|
|                  | 3. Press the submit button.    | 2. The form accepts only valid|
|                   |                               | data. All fields required but |
|                   |                               | the comments field.           |
|                    |                              | 3. The user is redirected to |
|                   |                               | the booking success page.     |
| --------------- | ------------------------- | ---------------------- | --------------------|
| Edit a booking    | 1. Go to the dashboard by       | 1. The booking cards are | 1. Pass.         |
|                   | clicking on the Bookings button.| displayed under the My   | 2. Pass.
|                   | 2. Click edit on one of your    | Bookings title.          | 3. Pass.
|                   | bookings.                       | 2. The user is redirected | 4. Pass.
|                   | 3. Change the data.             | to the edit_booking page.  |
|                   | 4. Press the save changes button.| 3. The user is abel to   |
|                   |                                  | change the desired field|
|                   |                                  | with valid data.          |
|                   |                                  | 4. The user is redirected to |
|                   |                                 | the dashboard, the card displayed|
|                   |                                 | with the updated data. |  
| --------------- | ------------------------- | ---------------------- | --------------------|
| Delete a booking  | 1. Go to the dashboard by       | 1. The booking cards are | 1. Pass.
|                   | clicking on the Bookings button.| displayed under the My   | 2. Pass.
|                   | 2. Click delete on one of your  | Bookings title.         |  3. Pass.
|                   | bookings.                        | 2. The user is redirected |
|                   | 3. Click on the Confirm Delete button.| to the delete_booking page.|
|                   |                                   | 3. The user is redirected to the |
|                   |                                   | dashboard. The deleted booking |
|                   |                                   | is not displayed anymore.       |
| --------------- | ------------------------- | ---------------------- | --------------------|