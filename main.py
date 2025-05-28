from flask import Flask, render_template, redirect, url_for, request, session
from services import auth_service, board_service, user_service

app = Flask(__name__)
app.secret_key = "your-secret-key"  # для сессий

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    boards = board_service.get_user_boards(session['user'])
    return render_template('dashboard.html', boards=boards)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = auth_service.login(request.form['username'], request.form['password'])
        if user:
            session['user'] = user
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        auth_service.register(request.form)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/board/<int:board_id>')
def board(board_id):
    board = board_service.get_board(board_id)
    return render_template('board.html', board=board)

@app.route('/profile')
def profile():
    user = user_service.get_user(session['user'])
    return render_template('profile.html', user=user)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        user_service.change_password(session['user'], request.form['new_password'])
        return redirect(url_for('index'))
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)
