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
All the cars in the DB
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
### /cars/<string:carName>
#### GET
Returns data about the individual car based on the model name in the URL
#### DEL
Deletes car from DB
#### PUT
Allows for editing of car data (NOTE: Any data can be changed including the name itself. The car will then be accessible only by the new name)
Data format:
```
{
	"name": <name>,
	"make": <manufacturer>,
	"power": <power:integer>
}
```
### /drivers
All the drivers in the DB
#### GET
Returns a list of all the drivers in the DB
#### POST
Allows user to add driver to DB
Data Format:
```
{
	"driver": <driver_name>,
	"team": <driver's_racing_team>,
	"rating": <performance_rating:float>
}
```
### /drivers/`<driver:name>`
#### GET
Returns the driver by the specific name in the URL.
#### DELETE
Deletes a specific driver based on URL
#### PUT
Edits a specific driver based on URL.
Data Format:
```
{
	"driver": <driver_name>,
	"team": <driver's_racing_team>,
	"rating": <performance_rating:float>
}
```

## NOTE: Capitalization does not matter. All input turns into uppercase! All spaces turn into '_'s





