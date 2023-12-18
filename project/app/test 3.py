def make_dict(keys, values):
    dict = {}
    for i in range(min(len(keys), len(values))):
        dict[keys[i]] = values[i]
    for key in keys[min(len(keys), len(values))::]:
        dict[key] = None
    return dict

def make_dict(keys, values):
    dict = {keys[i]: values[i] for i in range(min(len(keys), len(values)))}
    for key in keys[min(len(keys), len(values))::]:
        dict[key] = None
    return dict