def max_aggregate(tup):
    l = []
    for i in tup:
        if i[0] not in l:
            l.append(i[0])
    res = []
    for i in l:
        res.append(tup[tup.index(i)+1:].index(max(tup,key = lambda x:x[1])))
    return max(tup,key = lambda x:x[1]),sum(res)

def test_function():
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)

test_function()

# Code by Sanskar
#*******************************************
# Without Test Case
def max_aggregate(tup):
    l = []
    for i in tup:
        if i[0] not in l:
            l.append(i[0])
    res = []
    for i in l:
        res.append(tup[tup.index(i)+1:].index(max(tup,key = lambda x:x[1])))
    return max(tup,key = lambda x:x[1]),sum(res)

# With Test Case
def test_function():
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)

test_function()

# Code by Sanskar
#*******************************************
"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==