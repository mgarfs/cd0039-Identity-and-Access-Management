import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
db_drop_and_create_all()

# ROUTES

@app.route('/drinks')
def get_drinks():
    """ GET /drinks - public endpoint
    Returns the list of drinks with short description:
    { 
      "drinks: [
        {
          "id": 1,
          "recipe": [
            {
              "color": "blue",
              "parts": 1
            }
          ],
          "title": "water"
        },
        ...
      ],
      "success": true,
    }
    """
    # @TODO add authentificaiton and authorization
    drinks=Drink.query.all()
    all_drinks = [drink.short() for drink in drinks]
    return jsonify({
        "success": True,
        "drinks": all_drinks
    })


@app.route('/drinks-detail')
def get_drinks_detail():
    """ GET /drinks-detail - requires 'get:drinks-detail' permission
    Returns the list of drinks with detailed (long) description:
    { 
      "drinks: [
        {
          "id": 1,
          "recipe": [
            {
              "color": "blue",
              "name": "water",
              "parts": 1
            }
          ],
          "title": "water"
        },
        ...
      ],
      "success": true,
    }
    """
    # @TODO add authentificaiton and authorization
    drinks=Drink.query.all()
    all_drinks = [drink.long() for drink in drinks]
    return jsonify({
        "success": True,
        "drinks": all_drinks
    })

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
