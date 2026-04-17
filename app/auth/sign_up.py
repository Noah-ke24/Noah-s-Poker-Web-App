from app.auth import auth_bp

@auth_bp.route('/methods/sign_up', methods=['POST'])
def sign_up():
    print("Sign up route called")

    return "Sign up successful"