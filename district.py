import requests

url = "https://api.covid19india.org/state_district_wise.json"
r = requests.get(url = url)
data = r.json()
dict = { }

# assuming we got this 'Tamil Nadu' from api or from any other function user requested
state = data['Tamil Nadu']['districtData']

for i in state:
    # have added '1' to all delta to check addition
    # TODO: check and remove this added 1 -> Harish
    state[i]['delta']['confirmed'] += 1
    print('confirmed cases in ', i, state[i]['confirmed'], 'delta total ', state[i]['delta']['confirmed'])
    # adding confirmed and delta confirmed cases
    totalConfirmed = state[i]['confirmed']+state[i]['delta']['confirmed']
    print('Total confirmed ', totalConfirmed)

    dict[i] = {
        'totalConfirmed': totalConfirmed,
        'city': i
    }

print('Final',dict)
# TODO: remove loggers -> Harish