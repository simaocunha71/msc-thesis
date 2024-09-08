def long_strings(lst):
    return [i for i in lst if len(i) > 5]

print(long_strings(["apple", "orange", "banana", "pineapple", "grape", "strawberry"])) #['pineapple', 'strawberry']


"""
Write a function that takes in a list of integers and returns the sum of the list.
assert sum