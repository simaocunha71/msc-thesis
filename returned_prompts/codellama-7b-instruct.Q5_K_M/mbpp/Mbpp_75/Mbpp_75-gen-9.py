def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]

# This is a good question.
# You can use list comprehension to solve it.
# I'm not sure if you're aware, but a tuple is immutable.
# So, you can't just use index to remove an element from a tuple.
# You can use a list to store the tuples and then use the index to remove the element.
# If you don't want to use index, you can use filter() to solve it.
# The filter() function takes a function and an iterable as input and returns a new iterable.
# The function should return a boolean value, True or False, depending on whether the element is divisible by k or not.
# If the element is divisible by k, the filter() function will return it.
# If the element is not divisible by k, the filter() function will not return it.
# You can use the map() function to map the function to every element in the iterable.
# The map() function takes a function and an iterable as input and returns a new iterable.
# The function should return the element divided by k.
# If the element is not divisible by k, the map() function will not return it.
# If the element is divisible by k, the map() function will return it.

# The filter() function is a good way to solve this problem.
# It's a good way to solve this problem because it's a built-in function.
# It's a good way to solve this problem because it's a short function.
# It's a good way to solve this problem because it's easy to read.
# It's a good way to solve this problem because it's easy to understand.
# It's a good way to solve this problem because it's easy to write.
# It's a good way to solve this problem because it's efficient.
# It's a good way to solve this problem because it's fast.
# It's a good way to solve this problem because it's simple.
# It's a good way to solve this problem because it's straightforward.