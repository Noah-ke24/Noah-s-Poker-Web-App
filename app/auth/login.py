from app.auth import auth_bp

@auth_bp.route('/methods/login', methods=['POST'])
def login():
    print("Login route called")

    return "Login successful"