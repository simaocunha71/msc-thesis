def transform_dict(dictionary, function):
    new_dict = {}
    for k, v in dictionary.items():
        new_dict[k] = function(v)
    return new_dict

# print(transform_dict({1: 2, 2: 3}, lambda x: x+1 ))

"""
Write a function that takes in a dictionary of numbers and a function that takes in one number and returns one number. It should apply the function to the value associated with each key in the dictionary, if the value is not None. If the value is None, it should leave the key unchanged. It should return a new dictionary mapping each original key to the transformed value.

assert transform_dict({1: 2, 2