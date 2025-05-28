import hashlib

# Простая "база данных" в памяти
users_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(form):
    username = form['username']
    password = form['password']
    if username in users_db:
        return False
    users_db[username] = {
        'username': username,
        'password': hash_password(password),
        'about': ''
    }
    return True

def login(username, password):
    user = users_db.get(username)
    if user and user['password'] == hash_password(password):
        return username
    return None
