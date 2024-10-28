# Here's a solution using list comprehension:
def sum_squares(lst):
    return sum([int(i) ** 2 for i in lst])
# Here's a solution using a for loop:
def sum_squares(lst):
    total = 0
    for i in lst:
        total += int(i) ** 2
    return total


# Here's a solution using a while loop:
def sum_squares(lst):
    total = 0
    i = 0
    while i < len(lst):
        total += int(lst[i]) ** 2
        i += 1
    return total

# Here's a solution using a for loop with a function:
def sum_squares(lst):
    def square(x):
        return int(x) ** 2
    total = 0
    for i in lst:
        total += square(i)
    return total

# Here's a solution using a while loop with a function:
def sum_squares(lst):
    def square(x):
        return int(x) ** 2
    total = 0
    i = 0
    while i < len(lst):
        total += square(lst[i])
        i += 1
    return total

# Here's a solution using a for loop with a lambda function:
def sum_squares(lst):
    return sum([i ** 2 for i in lst])

# Here's a solution using a while loop with a lambda function:
def sum_squares(lst):
    total = 0
    i = 0
    while i < len(lst):
        total += (lambda x: x ** 2)(lst[i])
        i += 1
    return total

# Here's a solution using a for loop with a map function:
def sum_squares(lst):
    return sum(map(lambda x: int(x) ** 2, lst))

# Here's a solution using a while loop with a map function:
def sum_squares(lst):
    total = 0
    i