from flask import Blueprint 

test_bp = Blueprint('test', '__name__name')

@test_bp.route('/test', methods=['GET'])
def test():
    return {"abc":"test"}