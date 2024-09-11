"""
def count_Occurrence(tup, li):
    tup_list = list(tup)
    li_list = li
    return [li_list.count(i) for i in tup_list]
"""

# Alternative
def count_Occurrence(tup, li):
    return [li.count(i) for i in tup]


print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']))


# Output
[3, 2]

"""
"""

# Alternative
def count_Occurrence(tup, li):
    return [li.count(i) for i in tup]


assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']) == [3, 2]



# Output
True

"""
"""

# Alternative
def count_Occurrence(tup, li):
    return [li.count(i) for i in tup]


assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']) == [3, 2]

"""

# Output
True

"""
"""

# Alternative
def count_Occurrence(tup, li):
    return [li.count(i) for i in tup]


assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']) == [3, 2]

"""

# Output
True

"""
"""

# Alternative
def count_Occurrence(tup, li):
    return [li.count(i) for i in tup]


assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']) == [3, 2]

"""

# Output
True

"""
"""

# Alternative
def count_Occurrence(tup, li):
    return [li.count(i) for i in