from flask import Blueprint 
import os

test_bp = Blueprint('test', '__name__name')

@test_bp.route('/test', methods=['GET'])
def test():
    print("dsfggdgd")
    print(os.getenv("DATABASE_URL"))
    return {"abc":"test7"}