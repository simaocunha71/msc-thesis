def expensive_items(data, n):
    sorted_data = sorted(data, key = lambda x: x['price'], reverse = True)
    return sorted_data[:n]