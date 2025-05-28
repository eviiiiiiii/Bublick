# Примитивная база досок и карточек
boards_db = {
    1: {
        'id': 1,
        'title': 'Рабочая доска',
        'columns': {
            'Tasks': [],
            'In Progress': [],
            'Test': [],
            'Done': [],
        },
        'users': ['admin']
    }
}

def get_user_boards(username):
    return [board for board in boards_db.values() if username in board['users']]

def get_board(board_id):
    return boards_db.get(board_id)
