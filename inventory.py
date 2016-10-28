from flask import abort
from flask import redirect
from flask import render_template
from flask import url_for
from os import urandom
import json

from database_connection import DatabaseConnection
from globals import globals

# Handles the inventory routes.

class Inventory:
    def __init__(self):
        self.b58 = globals.base58_hashids
        self.encode_id = globals.encode_id
    def __can_index(self, session):
        return 'is_student' in session and session['is_student']

    def __can_show(self, session):
        return 'is_student' in session and session['is_student']

    def __can_edit(self, session):
        return 'is_officer' in session and session['is_officer']

    def __can_update(self, session):
        return 'is_officer' in session and session['is_officer']

    def index(self, request, session):
        if request.method == 'GET':
            if 'person_id' not in session:
                abort(403)
            with DatabaseConnection() as db:
                inventory, _ = db.get_table("inventory")
                db.select(inventory)
            return render_template('inventory/index.html', items=db.fetchall())
        abort(405)
