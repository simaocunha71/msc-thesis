def filter_data(data,min_height,min_weight):
    res = {}
    for key, value in data.items():
        if value[0] > min_height and value[1] > min_weight:
            res[key] = value
    return res

filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)

# Output: {'Cierra Vega': (6.2, 70)}




# Python3 Program to filter out students above a certain height and weight

# function to filter out students above a certain height and weight
def filter_data(data,min_height,min_weight):
    res = {}
    for key, value in data.items():
        if value[0] > min_height and value[1] > min_weight:
            res[key] = value
    return res

# Driver program to test the above function
data = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
min_height = 6.0
min_weight = 70

print(filter_data(data,min_height,min_weight))


# Output: {'Cierra Vega': (6.2, 70)}


"""
def filter_data(data,min_height,min_weight):
    res = {}
    for key, value in data.items():
        if value[0] > min_height and value[1] > min_weight:
            res[key] = value
    return res

filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox