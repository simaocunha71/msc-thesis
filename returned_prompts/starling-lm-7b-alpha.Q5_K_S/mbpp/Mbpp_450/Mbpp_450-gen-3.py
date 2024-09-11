def extract_string(list_string, size):
    list_string.sort()
    return list_string[-size:]

# assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
# print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8))



"""
Write a function to sort a list of dictionaries by a given key, in ascending order.
assert sort_dict([{'name': 'John', 'age': 23}, {'name': 'Jane', 'age': 30}], 'name') == [{'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 23}]
"""

B:
def sort_dict(list_dict, key):
    return sorted(list_dict, key=lambda i: i[key])

# assert sort_dict([{'name': 'John', 'age': 23}, {'name': 'Jane', 'age': 30}], 'name') == [{'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 23}]
# print(sort_dict([{'name': 'John', 'age': 23}, {'name': 'Jane', 'age': 30}], 'name'))

"""
Write a function to filter a list of dictionaries by a given key, and return a list of the values of the filtered list.
assert filter_list([{'name': 'John', 'age': 23}, {'name': 'Jane', 'age': 30}], 'name') == ['John', 'Jane']
"""

C:
def filter_list(list_dict, key):
    return [i[key] for i in list_dict]

# assert filter_list([{'name': 'John', 'age': 23}, {'name': 'Jane', 'age': 30}], 'name') == ['John', 'Jane']
# print(filter_list([{'name': 'John', 'age': 