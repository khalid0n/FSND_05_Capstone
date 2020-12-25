# Udacity's Full Stack Nanodegree - Capstone Project 
This project is for **Film Casting Agency**, we have 2 main resources, `actors` & `movies`

######user can do the following:
- create `actors` & `movies`
- delete `actors` & `movies`
- update `actors` & `movies`
- list all `actors` & `movies`

###Motivations
It's the final project in the nanodegree that covers all the topics introduced before.
doing this project ensures that I got the needed understanding for:
- creating & manipulating DBs through ORM using SQLAlchemy.
- Creating RESTful APIs that interacts with the application's Backend.
- Securing APIs with third-party solutions, in my case it's *Auth0*.
- Implementing roles-based access control (RBAC) to ensure Authenticity.
- Implementing unit-testing using python library *unittest*.
- Deploying Application to Heroku

## Getting Started
Application is accessible in this URL [https://khalid-fsnd-capstone.herokuapp.com/](https://khalid-fsnd-capstone.herokuapp.com/)

### Installing Dependencies

#### Virtual Env
create virtual environment to work with this project

```bash
python -m virtualenv env
source env/bin/activate
```


#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the `root` and running:
```bash
pip3 install -r requirements.txt
```

#### Running the server

Firstly, check that you're working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

### Unit Tests
To run the tests, run
```
python3 test_app.py
```

### Postman collection
the API's endpoints testing can be imported in postman through this file `FNSD_Capstone.postman_collection.json`


 
## API Reference

#### Error Handling

Errors are returned as JSON objects in the following format:
```
{
    "error": 404,
    "message": "Not Found",
    "success": false
}
```
The API will return four error types when requests fail:

- 401: Un-Authorized
- 404: Not Found
- 422: Unable To Process
- 500: Internal Server Error

### Endpoints

#### GET '/actors'
Auth: requires Assistant, Director or Executive Tokes. 
- Returns All Actors.
 ```
       {
    "actors": [
        {
            "age": 22,
            "gender": "M",
            "id": 2,
            "name": "Mouth"
        },
        {
            "age": 28,
            "gender": "F",
            "id": 3,
            "name": "Sarah"
        },
        {
            "age": 40,
            "gender": "F",
            "id": 4,
            "name": "Julia"
        },
        {
            "age": 50,
            "gender": "M",
            "id": 5,
            "name": "Brad"
        }
    ],
    "success": true
}
```
     
#### GET '/movies'
Auth: requires Assistant, Director or Executive Tokes. 
- Returns All Movies.
```
{
    "actors": [
        {
            "id": 1,
            "release_date": "2018-10",
            "title": "Interstellar"
        },
        {
            "id": 2,
            "release_date": "2010-01",
            "title": "Inception"
        },
        {
            "id": 3,
            "release_date": "1999-08",
            "title": "American Beauty"
        },
        {
            "id": 4,
            "release_date": "2010-10",
            "title": "Inception2"
        },
        {
            "id": 5,
            "release_date": "2004-05",
            "title": "Beautiful Mind"
        }
    ],
    "success": true
}
```
#### DELETE '/actors/Id'
Auth: requires Director or Executive Tokes. 
- Deletes the actor with given **id**.
- returns the deleted actor's id.
```
{
    "deleted": 1,
    "success": true
}
```
     
#### DELETE '/movies/id'
Auth: requires Executive Tokes. 
- Deletes the movie with given **id**.
- returns the deleted movie's id.
```
{
    "deleted": 6,
    "success": true
}
```
#### POST '/actors'
Auth: requires Director or Executive Tokes. 
- creates actor
- returns the created actor's attributes
```
{
    "name": "Brad",
    "age": 40,
    "gender": "M"
}
```
   
#### POST '/movies'
Auth: requires Executive Tokes. 
- creates movie
- returns the created movie's attributes
```
{
    "title": "Beautiful Mind",
    "release_date": "2004-05"
}
```
#### PATCH '/actors/id'
Auth: requires Director or Executive Tokes. 
- updates actor's attributes based on input and given **id**
- returns the actor's attributes
```
{
    "age": 50
}
```
 #### PATCH '/movies/id'
Auth: requires Director or Executive Tokes. 
- updates movie's attributes based on input and given **id**
- returns the movies's attributes
```
{
    "release_date": "1999-08"
}
```
