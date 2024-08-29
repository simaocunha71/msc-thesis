def sort_counter(dict):
    return sorted(dict.items(), key = lambda x: x[1])

print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))


