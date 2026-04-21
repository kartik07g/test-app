from flask import Blueprint, request, jsonify
from Resources.Users.UserService import UserService

auth_bp = Blueprint('auth', __name__)
service = UserService()


@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "email and password are required"}), 400

    token = service.login(data["email"], data["password"])
    if not token:
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({"access_token": token})
