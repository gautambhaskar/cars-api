# Documentation for Cars API
RESTful API built with Python and Flask.


This API allows for saving and interacting with data about drivers and cars on an SQLite DB. To do so, you can use basic HTTP
commands like PUT, POST, GET, and DELETE...

## Endpoints:
### /register
Used to Register Users (All commands require Token Authentication so user authentication is required)
Simply pass:
```
{
	"username": "<desired_username>",
	"password": "<desired_password>"
}
```
