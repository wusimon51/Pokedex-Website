from flask import render_template, url_for
from pokedex import app
from pokedex.models import Pokemon


poke_list = Pokemon.query.all()
@app.route('/')
@app.route('/pokemon')
def pokemon():
    return render_template('index.html', poke_list=poke_list)
