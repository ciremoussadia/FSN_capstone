import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie
from auth import requires_auth, AuthError


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', '*')
        return response

    @app.route('/actors')
    @requires_auth('read:actors')
    def read_actors(payload):
        actors = Actor.query.all()
        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        }), 200

    @app.route('/actors', methods=['POST'])
    @requires_auth('create:actors')
    def create_actor(payload):
        return jsonify({}), 200

    @app.route('/actors/<actor_id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actor(payload, actor_id):
        return jsonify({}), 200

    @app.route('/actors/<actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        return jsonify({}), 200

    @app.errorhandler(AuthError)
    def auth_error(AuthError):
        return jsonify({
            'error': 401,
            'message': 'Authentication Error'
        }), 401

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
