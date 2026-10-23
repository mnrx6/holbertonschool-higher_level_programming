#!/usr/bin/python3
"""Simple API with Basic and JWT authentication."""

import os
import secrets
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = os.environ.get(
    "JWT_SECRET_KEY", secrets.token_hex(32)
)
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password."""
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return users[username]

    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Basic authentication route."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Login and create JWT token."""
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if username in users and isinstance(password, str):
        if check_password_hash(users[username]["password"], password):
            token = create_access_token(identity=username)
            return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """JWT protected route."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Admin only route."""
    username = get_jwt_identity()

    if username not in users or users[username]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def unauthorized_error(err):
    """Handle missing tokens."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_error(err):
    """Handle invalid tokens."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_error(jwt_header, jwt_payload):
    """Handle expired tokens."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked tokens."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def fresh_token_error(jwt_header, jwt_payload):
    """Handle tokens that are not fresh."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
