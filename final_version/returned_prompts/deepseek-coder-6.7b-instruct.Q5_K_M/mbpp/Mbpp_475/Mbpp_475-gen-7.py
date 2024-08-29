def sort_counter(dic):
    return sorted(dic.items(), key=lambda kv: kv[1])

print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))

"""
Output:
[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

This function sorts a dictionary by value by using the built-in sorted function along with a lambda function that defines the sorting key as the dictionary value.

"""
