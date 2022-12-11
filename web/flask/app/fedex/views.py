from flask import render_template, jsonify

from app.fedex import fedex
from app.models.users import Users


@fedex.route('/')
def index():
    return render_template('fedex/users.html', users=Users().get_users)


@fedex.route('/json_example')
def json_example():
    return jsonify({'operation': 'show', 'data': {'id': 42, 'result': True}})
