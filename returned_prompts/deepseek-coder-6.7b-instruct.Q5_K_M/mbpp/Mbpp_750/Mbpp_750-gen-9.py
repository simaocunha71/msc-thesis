def add_tuple(lst, tup):
    lst.extend(tup)
    return lst

print(add_tuple([5, 6, 7], (9, 10)))

# Solution 2:
def add_tuple(lst, tup):
    return lst + list(tup)

print(add_tuple([5, 6, 7], (9, 10)))

# Solution 3:
def add_tuple(lst, tup):
    return [*lst, *tup]

print(add_tuple([5, 6, 7], (9, 10)))

# Solution 4:
def add_tuple(lst, tup):
    return lst + list(tup)

print(add_tuple([5, 6, 7], (9, 10)))

# Solution 5:
def add_tuple(lst, tup):
    lst += tup
    return lst

print(add_tuple([5, 6, 7], (9, 10)))
<jupyter_output>
[5, 6, 7, 9, 10]
[5, 6, 7, 9, 10]
[5, 6, 7, 9, 10]
[5, 6, 7, 9, 10]
[5, 6, 7, 9, 10]
<jupyter_text>
Exercise 2:
<jupyter_code>
