def reverseLookup(u_dict, u_value):
    key_list = []
    for key in u_dict:
        if u_dict[key] == u_value:
            key_list.append(key)
        
    return key_list


model_car = {
    'Fiesta' : 'Ford',
    'Mustang': 'Ford',
    'Puma': 'Ford',
    'Kuga': 'Ford',
    'Punto': 'Fiat',
    'Cinquecento': 'Fiat',
    'Panda': 'Fiat',
    '206': 'Peugeot'
}

print(reverseLookup(model_car, 'Fiat'))

