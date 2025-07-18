from flask import Blueprint, render_template_redirect
from . import db
from models import emails


admin_bp = Blueprint('admin', __name__)
