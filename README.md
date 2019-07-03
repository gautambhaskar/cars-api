# Documentation for Cars API
RESTful API built with Python and Flask.


This API allows for saving and interacting with data about drivers and cars on an SQLite DB. To do so, you can use basic HTTP
commands like PUT, POST, GET, and DELETE...

## Endpoints:
NOTE: All requests give DECENT error messages
### /register (POST)
Used to Register Users (All commands require Token Authentication so user authentication is required)
Simply pass:
```
{
	"username": "<desired_username>",
	"password": "<desired_password>"
}
```

### /auth (POST)
Used to authenticate user. Return a JWT access_token. Must do authentication even if user has just been registered
```
{
	"username": "<chosen_username>",
	"password": "<chosen_password>"
}
```
The received token must then be copied and used in all further requests. To do so set the "Authorization" Request Header to 
```
'JWT <access_token>'
```

### /cars
#### GET
Returns a list of all the cars in the DB.

#### POST
Allows user to add cars to DB.
Simply add user details to request similar to this:
```
{
	"name": <name>,
	"make": <manufacturer>,
	"power": <power:integer>
}
```
