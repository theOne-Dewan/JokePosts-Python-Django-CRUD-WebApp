# Python Django CRUD WebApp

This blog posting web app allows users to register and log into their accounts with full user authentication/verification via Bcrypt, then Creat-Read-Update-Delete posts. The backend server is run on and managed on the Django framework and the user/content data is stored on a SQLite server within the framework.

## Languages/Frameworks/Libraries Used

* Python
* Django
* Bcrypt
* SQLite
* HTML
* CSS
* Bootstrap

## Key Features

* Allows storage of user registration data and posts data via the built in SQLite.
* Allows CRUD commands on said data.
* Notifies uses of empty fields, incorrent range of input size, incorrect format of email input and if the password/passwordConfirmation do not match with error messages under the fields.
* Permits only the user who is signed in to edit or delete their data, and prevents them from tampering with other users posts.
* Prevents anyone from accessing the website without successfully registering and logging in due to strict session management.
* Passwords are strongly hashed via Bcrypt, then stored in the database securely when registering. When logging in functions in the backend uses Bcrypt to validate the login attempt.


