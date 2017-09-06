import json
from os import listdir, path

commands = ['!pronouns', '!mypronouns']

json_file = path.join(path.dirname(path.abspath(__file__)), 'pronouns.json')

if 'pronouns.json' not in listdir(path.dirname(path.abspath(__file__))):
    pronouns = {}
    with open(json_file, 'w') as f:
        json.dump(pronouns, f)

with open(json_file) as f:
    pronouns = json.load(f)

def my_pronouns(user, p):
    pronouns[user] = p
    with open(json_file, 'w') as f:
        json.dump(pronouns, f, sort_keys=True, indent=4)
    return ('message', '{}: Your pronouns have been saved'.format(user))

def get_pronouns(user):
    if user in pronouns:
        msg = 'Pronouns for {}: {}'.format(user, pronouns[user])
    elif user == '':
        msg = 'Please enter a valid user, or use !mypronouns to declare your pronouns'
    else:
        msg = '{} has not declared any pronouns'.format(user)
    return ('message', msg)

def run(**kwargs):
    cmd = kwargs['cmd']
    user = kwargs['nick']
    p = kwargs['arg']
    if cmd == '!pronouns':
        return get_pronouns(user)
    elif cmd == '!mypronouns':
        return my_pronouns(user, p)
