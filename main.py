from flask import Flask, jsonify, request
from contact_service import ContactService
from validators import is_email, is_phone_number
from time import strftime
import logging, traceback
from logging.handlers import RotatingFileHandler

def create_app(test_config=None):
    app = Flask(__name__)
    contact_service = ContactService(f"data/{"test_contacts" if test_config and test_config['TESTING'] else "contacts"}.json")

    @app.route("/contacts", methods=["POST"])
    def add_contact():
        data = request.get_json()
        if not data:
            return jsonify({"error": "Empty request body"}), 400
        elif not all([field in data for field in ["name", "email", "phone_number"]]):
            return jsonify({"error": "Missing required fields"}), 400
        elif not is_email(data["email"]):
            return jsonify({"error": "Invalid email format"}), 400
        elif not is_phone_number(data["phone_number"]):
            return jsonify({"error": "Invalid phone number format"}), 400
        elif contact_service.is_email_or_phone_number_existed(data["email"], data["phone_number"]):
            return jsonify({"error": "Email or phone_number existed"}), 400
        contact = contact_service.add_contact(app, data["name"], data["email"], data["phone_number"])
        return jsonify({"message": f"Added contact with ID: {contact['_id']}"})

    @app.after_request
    def after_request(response):
        if not app.config['TESTING']:
            logger.info(f"[INFO] {strftime('[%Y-%m-%d %H:%M:%S]')} {request.remote_addr} {request.method} {request.scheme} {request.full_path} {response.status}")
        return response

    @app.errorhandler(Exception)
    def exceptions(e):
        if not app.config['TESTING']:
            logger.error(f"[ERROR] {strftime('[%Y-%m-%d %H:%M:%S]')} {request.remote_addr} {request.method} {request.scheme} {request.full_path} \n{traceback.format_exc()}")
        return e.error

    return app


if __name__ == '__main__':
    logger = logging.getLogger('tdm')
    logger.setLevel(logging.INFO)
    logger.addHandler(RotatingFileHandler('app.log', maxBytes=100000, backupCount=3))
    create_app().run()