def drop_empty(dic):
    return {key: value for key, value in dic.items() if value}

print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}))

