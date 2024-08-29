def sort_counter(dict):
    return sorted(dict.items(), key=lambda x: x[1])

#Test
print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))

#Output: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

"""
Explanation:
In the function, we are using the built-in function sorted(). It takes two arguments: the iterable (dict.items()) and the key (lambda x: x[1]). The key argument is a function that specifies a single argument to be passed to sorted() to determine the sort order. In this case, we are using a lambda function to sort the dictionary items based on their values.
"""
<jupyter_output>
[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
<jupyter_text>
Question 2:
<jupyter_code>
"""
