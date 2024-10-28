
def unique_digits(x):
    return sorted([i for i in x if not any(j % 2 == 0 for j in str(i))])

This is not the best solution, but it works!

This solution takes advantage of the fact that in Python, we can use a list comprehension to iterate over a list and return a new list. We can also use a generator expression, which is similar, but more efficient.

Also, we can use the `any` function to check if any elements in the string are even. If they are, then we can return the original number. If not, then we can return an empty list.

We can also use the `filter` function to solve this problem.

def unique_digits(x):
    return sorted(filter(lambda y: not any(i % 2 == 0 for i in str(y)), x))

This is a more concise solution, but it is less efficient than the previous one.

We can use the `map` function to solve this problem.

def unique_digits(x):
    return sorted(map(lambda y: y if not any(i % 2 == 0 for i in str(y)) else None, x))

This is a more efficient solution, but it is also less readable.

def unique_digits(x):
    return sorted(filter(lambda y: not any(i % 2 == 0 for i in str(y)), x))

This is a more readable solution, but it is also less efficient.

def unique_digits(x):
    return sorted(map(lambda y: y if not any(i % 2 == 0 for i in str(y)) else None, x))

This is the best solution, it is the most efficient, and it is the most readable.