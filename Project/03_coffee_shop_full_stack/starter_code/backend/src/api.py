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
Uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one record to the database
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
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
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
    drinks=Drink.query.all()
    all_drinks = [drink.long() for drink in drinks]
    return jsonify({
        "success": True,
        "drinks": all_drinks
    })


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(payload):
    """ POST /drinks - requires the 'post:drinks' permission
    Creates a new row in the drinks table
    Request body should match the drink.long() data representation

    Returns status code 200 and json:
    {
        "success": True, 
        "drinks": drink
    }
    - where drink is an array containing only the newly created drink (long description)
    or appropriate status code indicating reason for failure
    """
    body = request.get_json()
    new_title = body.get("title", None)
    new_recipe = body.get("recipe", None)
    if new_title is None or new_recipe is None:
        abort(422)
    else:
        try:
            drink = Drink(title=new_title, recipe=str(new_recipe).replace("'",'"'))
            drink.insert()
            return jsonify({
                "success": True,
                "drinks": drink.long()
            })
        except:
            abort(422)


@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, drink_id):
    """ PATCH /drinks/<id> - requires the 'patch:drinks' permission
        - where <id> is the existing model id
    Updates the corresponding row for <id> or responds with a 404 error if <id> is not found
    Request body should match the drink.long() data representation

    Returns status code 200 and json:
    {
        "success": True, 
        "drinks": drink
    }
    - where drink is an array containing only the updated drink (long description)
    or appropriate status code indicating reason for failure
    """
    drink = Drink.query.filter(Drink.id==drink_id).one_or_none()
    body = request.get_json()
    new_title = body.get("title", None)
    new_recipe = body.get("recipe", None)
    app.logger.info(new_title)
    app.logger.info(str(new_recipe).replace("'",'"'))
    if new_title is None or new_recipe is None:
        abort(422)
    else:
        try:
            drink.title = new_title
            drink.recipe = str(new_recipe).replace("'",'"')
            drink.update()
            return jsonify({
                "success": True,
                "drinks": drink.long()
            })
        except:
            abort(422)

@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, drink_id):
    """ DELETE /drinks/<id> - requires the 'delete:drinks' permission
        - where <id> is the existing drink id
    Deletes the corresponding row for <id> or responds with a 404 error if <id> is not found

    Returns status code 200 and json:
    {
        "success": True,
        "delete": drink_id
    } 
    - where drink_id is the id of the deleted record
    or appropriate status code indicating reason for failure
    """
    try:
        drink = Drink.query.filter(Drink.id==drink_id).one_or_none()
        if drink is None:
            abort(404)
        else:
            drink.delete()
            return jsonify({
                "success": True,
                "delete": drink_id
            })
    except:
        abort(422)


# Error Handling
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


