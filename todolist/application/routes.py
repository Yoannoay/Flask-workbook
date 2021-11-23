from application import app, db
from application.models import Tasks

@app.route('/create/task')
def create_task():
    new_task = Tasks(description="New task")
    db.session.add(new_task)
    db.session.commit()
    return f"task with id {new_task.id} added to database"

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    all_names = []
    for name in all_tasks:
        all_names.append(name.description)
    return all_names
    

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     db.session.commit()
#     return first_game.name

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     db.session.commit()
#     return first_game.name

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     db.session.commit()
#     return first_game.name