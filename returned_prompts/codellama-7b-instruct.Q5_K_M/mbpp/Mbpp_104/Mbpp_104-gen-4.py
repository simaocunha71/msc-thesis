def sort_sublists(lst):
    return [[*sorted(sublist)] for sublist in lst]

# OR

def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

# OR

def sort_sublists(lst):
    return [[*sorted(sublist)] for sublist in map(sorted, lst)]

# OR

def sort_sublists(lst):
    return list(map(sorted, map(sorted, lst)))

# OR

def sort_sublists(lst):
    return list(map(sorted, map(lambda x: sorted(x), lst)))

# OR

def sort_sublists(lst):
    return list(map(sorted, map(lambda x: sorted(x, reverse=True), lst)))

# OR

def sort_sublists(lst):
    return list(map(sorted, map(lambda x: sorted(x, reverse=True), lst), reverse=True))

# OR

def sort_sublists(lst):
    return list(map(lambda x: sorted(x, reverse=True), map(lambda x: sorted(x), lst)))

# OR

def sort_sublists(lst):
    return list(map(lambda x: sorted(x, reverse=True), map(lambda x: sorted(x), lst), reverse=True))

# OR

def sort_sublists(lst):
    return list(map(lambda x: sorted(x, reverse=True), map(lambda x: sorted(x), lst), reverse=True))

# OR

def sort_sublists(lst):
    return list(map(lambda x: sorted(x, reverse=True), map(sorted, lst), reverse=True))

# OR

def sort_sublists(lst):
    return list(map(lambda x: sorted(x, reverse=True), map(sorted, lst), reverse=True))

# OR

def sort_sublists(lst):
    return list(map(sorted, map(lambda x: sorted(x), lst), reverse=True))

# OR

def sort_sublists(lst):
    return list(map(sorted,