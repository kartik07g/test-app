from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Resources.Users.UserService import UserService

user_bp = Blueprint('users', __name__)
service = UserService()


def user_to_dict(user):
    return {
        "user_id": user.user_id,
        "email": user.email,
        "status": user.status,
        "created_at": str(user.created_at) if user.created_at else None,
        "updated_at": str(user.updated_at) if user.updated_at else None,
    }


@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = service.get_all_users()
    return jsonify([user_to_dict(u) for u in users])


@user_bp.route('/users/<user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = service.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_to_dict(user))


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "email and password are required"}), 400
    user = service.create_user(data)
    return jsonify(user_to_dict(user)), 201


@user_bp.route('/users/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    user = service.update_user(user_id, data)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_to_dict(user))


@user_bp.route('/users/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    success = service.delete_user(user_id)
    if not success:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"})
