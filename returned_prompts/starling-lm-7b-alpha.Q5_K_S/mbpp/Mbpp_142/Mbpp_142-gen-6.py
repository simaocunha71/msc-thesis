def count_samepair(a,b,c):
    n1 = len(a)
    n2 = len(b)
    n3 = len(c)
    if n1 != n2 or n2 != n3:
        return 0
    else:
        count = 0
        for i in range(n1):
            if a[i] == b[i] == c[i]:
                count += 1
        return count

def test_count_samepair():
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]) == 3

test_count_samepair()



"""
def count_samepair(a, b, c):
    if len(a) != len(b) or len(b) != len(c):
        return 0
    else:
        count = 0
        for i in range(len(a)):
            if a[i] == b[i] == c[i]:
                count += 1
        return count

def test_count_samepair():
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]) == 3

test_count_samepair()
"""

"""
def count_samepair(a,b,c):
    lena = len(a)
    lenb = len(b)
    if lena != lenb:
        return 0
    else:
        count = 0
        for i in range(lena):
            if a[i] == b[i] == c[i]:
                count += 1
        return count

def test_count_samepair():
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2