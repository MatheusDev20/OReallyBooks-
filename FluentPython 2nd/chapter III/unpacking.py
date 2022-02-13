def dump(**kwargs):
    return kwargs['cpf']

params = {"cpf": '14032063680', "number": 1}
print(dump(**params))
