import requests

url = "https://api.covid19india.org/data.json"
r = requests.get(url = url)
data = r.json()
dict = { }

state = data['statewise']

for i in state:
    state = i['state']
    active = i['active']
    confirmed = i['confirmed'] + i['deltaconfirmed']
    death = i['deaths'] + i['deltadeaths']
    recovered = i['recovered'] + i['deltarecovered']
    lastupdatedtime = i['lastupdatedtime']
    print('confirmed cases in ', state, confirmed, ' active total ', active, ' death ', death, ' recovered', recovered, 'lastupdated at ', lastupdatedtime)

    dict[state] = {
        'state': state,
        'active': active,
        'confirmed': confirmed,
        'death': death,
        'recovered': recovered,
        'lastupdatedtime': lastupdatedtime
    }

print('Final',dict)
# TODO: remove loggers -> Harish