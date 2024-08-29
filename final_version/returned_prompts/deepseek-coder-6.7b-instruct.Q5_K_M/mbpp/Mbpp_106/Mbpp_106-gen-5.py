def add_lists(lst, tpl):
    return tpl + tuple(lst)

print(add_lists([5, 6, 7], (9, 10)))

# -------------------------------------
# Alternative solution using list comprehension
def add_lists(lst, tpl):
    return tpl + tuple([i for i in lst])

print(add_lists([5, 6, 7], (9, 10)))

# -------------------------------------
# Alternative solution using map function
def add_lists(lst, tpl):
    return tpl + tuple(map(lambda x: x, lst))

print(add_lists([5, 6, 7], (9, 10)))

# -------------------------------------
# Alternative solution using join and eval functions
def add_lists(lst, tpl):
    return eval(str(tpl) + '+' + str(tuple(lst)))

print(add_lists([5, 6, 7], (9, 10)))

# -------------------------------------
# Alternative solution using extend function
def add_lists(lst, tpl):
    tpl_list = list(tpl)
    tpl_list.extend(lst)
    return tuple(tpl_list)

print(add_lists([5, 6, 7], (9, 10)))

# -------------------------------------
# Alternative solution using * operator
def add_lists(lst, tpl):
    return tpl + (*lst,) )

print(add_lists([5, 6, 7], (9, 10)))

# -------------------------------------
# Alternative solution using for loop
def add_lists(lst, tpl):
    tpl_list = list(tpl)
    for i in lst:
        tpl_list.append(i)
    return tuple(tpl_list)

print(add_lists([5, 6, 7], (9, 10)))

# -------------------------------------
# Alternative solution using numpy concatenate function
import numpy as np
def add