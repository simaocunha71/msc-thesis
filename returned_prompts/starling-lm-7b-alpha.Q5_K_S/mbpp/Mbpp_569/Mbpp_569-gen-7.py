"""
def sort_sublists(sublists):
    sorted_sublists = []
    for sublist in sublists:
        sorted_sublist = sorted(sublist)
        sorted_sublists.append(sorted_sublist)
    return sorted_sublists
"""

def sort_sublists(sublists):
    sorted_sublists = []
    for sublist in sublists:
        sorted_sublist = sorted(sublist)
        sorted_sublists.append(sorted_sublist)
    return sorted_sublists

# assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]


def sort_sublists_v2(sublists):
    return [sorted(sublist) for sublist in sublists]

# assert sort_sublists_v2([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]


def sort_sublists_v3(sublists):
    return list(map(lambda sublist: sorted(sublist), sublists))

# assert sort_sublists_v3([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]


def sort_sublists_v4(sublists):
    return [sublist for sublist in sublists for _ in sublist]

# assert sort_sublists_v4([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]


def sort_sublists_v5(sublists):
    return [sorted(sublist) for sublist in sublists]

# assert sort_sublists_v