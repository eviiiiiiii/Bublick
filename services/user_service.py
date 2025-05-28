from services.auth_service import users_db

def get_user(username):
    return users_db.get(username)

def change_password(username, new_password):
    from services.auth_service import hash_password
    if username in users_db:
        users_db[username]['password'] = hash_password(new_password)
