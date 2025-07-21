from flask import Blueprint, render_template_redirect
from . import db
from models import emails

user_bp = Blueprint('user', __name__)

@user_bp.route()