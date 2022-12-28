# Flask-Website

## Package used

This website is a website in Python using the micro-framework Flask 2.x and all the
following packages:
* **sqlalchemy** in order to manage the database and to avoid recreating the storage of the application
* **werkzeug** This package is used in order to handle the hashing of the password before going into the user database.
* **LoginManager** The LoginManager class is inside of the flask_login package, it allows the developpers handling the user (creation, login, and so on...) easily.

## Architecture

2 blueprints is created, one for the authentication and another one for the view, and the note managment (like a basic CRUD about the written note).

## Reason

The application has been made in order to learn more about Flask, and also to learn how peoples are creating Flask application (using the application factory like in this project for instance). 

