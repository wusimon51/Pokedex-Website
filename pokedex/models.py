import requests
from pokedex import db


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    type_1 = db.Column(db.String(15), nullable=False)
    type_2 = db.Column(db.String(15))
    abilities = db.Column(db.String(30), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    base_xp = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    sp_atk = db.Column(db.Integer, nullable=False)
    sp_def = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    held_items = db.Column(db.String(20))
    sprite = db.Column(db.String(80))


def get_types(data):
    list = []
    list.append(data['types'][::-1][0]['type']['name'])
    if len(data['types']) == 1:
        list.append(None)
    else:
        list.append(data['types'][::-1][1]['type']['name'])
    return list


def get_abilities(data):
    list = []
    for ability in data['abilities']:
        list.append(ability['ability']['name'])
    return ', '.join(list)


def get_held_items(data):
    if len(data['held_items']) == 0:
        return None
    else:
        list = []
        for item in data['held_items']:
            list.append(item['item']['name'])
        return ', '.join(list)


def get_data():
    for id in range(1, 808):
        poke_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}/').json()
        poke_object = Pokemon(
            name=poke_data['name'],
            type_1=get_types(poke_data)[0],
            type_2=get_types(poke_data)[1],
            abilities=get_abilities(poke_data),
            height=poke_data['height'],
            weight=poke_data['weight'],
            base_xp=poke_data['base_experience'],
            hp=poke_data['stats'][5]['base_stat'],
            attack=poke_data['stats'][4]['base_stat'],
            defense=poke_data['stats'][3]['base_stat'],
            sp_atk=poke_data['stats'][2]['base_stat'],
            sp_def=poke_data['stats'][1]['base_stat'],
            speed=poke_data['stats'][0]['base_stat'],
            held_items=get_held_items(poke_data),
            sprite=poke_data['sprites']['front_default']
        )
        db.session.add(poke_object)
    db.session.commit()