"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""

def get_lucid(n):
    assert n<10
    res = []
    for i in range(0, int(math.sqrt((n-1)))+1):
        if (i % 2) == 1: # only odd numbers
            yield int(n - int(math.fabs(float(i)/float(2)) * (float(n)-int(float(i)/2))));
    return res;
