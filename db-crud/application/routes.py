from application import app, db
from application.models import Games

@app.route('/add/<name>')
def add(name):
    new_game = Games(name=name)
    db.session.add(new_game)
    db.session.commit()
    return f"Added {name} to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    json = {"games": []}
    for game in all_games:
        json["games"].append(game.name)
    return json

@app.route('/update/<int:id>/<name>')
def update(id, name):
    game = Games.query.get(id)
    game.name = name
    db.session.commit()
    return f"Updated game {game.id} name to {game.name}"

@app.route('/delete')
def delete():
    deleteable = Games.query.first()
    db.session.delete(deleteable)
    db.session.commit()
    return f"The first item has been deleted."

@app.route('/game-count')
def count():
    game_num = Games.query.all()
    return f"Total number of games: {len(game_num)} "

    
