def sort_counter(dic):
    return sorted(dic.items(), key=lambda x:x[1])

print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))

# Output:
# [('Math', 81), ('Physics', 83), ('Chemistry', 87)]

# This function works by using the built-in sorted function in Python. 
# The key argument of the sorted function is a function that takes a single argument and returns a key to use for sorting purposes.
# Here, we provide a lambda function that returns the value of each item in the dictionary for use as a sort key.
# The sorted function returns a list of tuples, which is the result of our function.

# If you want to sort the dictionary in descending order, you can simply add reverse=True argument to the sorted function:
# def sort_counter(dic):
#     return sorted(dic.items(), key=lambda x:x[1], reverse=True)
<jupyter_output>
<empty_output>
<jupyter_text>
