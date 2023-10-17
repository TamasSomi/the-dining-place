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


