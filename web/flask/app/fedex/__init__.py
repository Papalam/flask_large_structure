from flask import Blueprint


fedex = Blueprint('fedex', __name__)

from app.fedex import views
