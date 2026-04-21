from core.database import session_local
from models.Users import Users
from flask_jwt_extended import create_access_token


class UserService:

    def get_all_users(self):
        db = session_local()
        try:
            return db.query(Users).all()
        finally:
            db.close()

    def get_user_by_id(self, user_id):
        db = session_local()
        try:
            return db.query(Users).filter(Users.user_id == user_id).first()
        finally:
            db.close()

    def create_user(self, data):
        db = session_local()
        try:
            user = Users(email=data["email"], password=data["password"])
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        finally:
            db.close()

    def update_user(self, user_id, data):
        db = session_local()
        try:
            user = db.query(Users).filter(Users.user_id == user_id).first()
            if not user:
                return None
            for key in ("email", "password", "status"):
                if key in data:
                    setattr(user, key, data[key])
            db.commit()
            db.refresh(user)
            return user
        finally:
            db.close()

    def delete_user(self, user_id):
        db = session_local()
        try:
            user = db.query(Users).filter(Users.user_id == user_id).first()
            if not user:
                return False
            db.delete(user)
            db.commit()
            return True
        finally:
            db.close()

    def login(self, email, password):
        db = session_local()
        try:
            user = db.query(Users).filter(Users.email == email).first()
            if not user or user.password != password:
                return None
            return create_access_token(identity=user.user_id)
        finally:
            db.close()
