def max_aggregate(t):
    d={}
    for i in t:
        if i[0] in d:
            d[i[0]]+=i[1]
        else:
            d[i[0]]=i[1]
    return max(d.items(), key=lambda x:x[1])


# Here is the solution

"""
def max_aggregate(t):
    d={}
    for i in t:
        if i[0] in d:
            d[i[0]]+=i[1]
        else:
            d[i[0]]=i[1]
    return max(d.items(), key=lambda x:x[1])
"""

# Here is the test code

def test_max_aggregate():
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)

test_max_aggregate()

"""
"""

# End of Solution

# Python3 program to find maximum aggregate from the
# list of tuples

# Function to find maximum aggregate from the list of tuples
def max_aggregate(t):
    d={}
    for i in t:
        if i[0] in d:
            d[i[0]]+=i[1]
        else:
            d[i[0]]=i[1]
    return max(d.items(), key=lambda x:x[1])

# Test the above function
def test_max_aggregate():
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)

test_max_aggregate()

# This code is contributed by Rajput-Ji
```
