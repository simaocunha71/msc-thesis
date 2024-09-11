"""
def search(l):
    a = []
    for i in l:
        if l.count(i) == 1:
            a.append(i)
    return a

def test_search():
    assert search([1,1,2,2,3]) == [3]
    assert search([1,2,3,4,5]) == [1,5]
    print("All tests passed")

if __name__ == "__main__":
    test_search()
"""

def search(l):
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l[0]
    if l[0] != l[1]:
        return l[0]
    if l[-1] != l[-2]:
        return l[-1]
    mid = len(l) // 2
    if l[mid] != l[mid-1]:
        return l[mid]
    return search(l[:mid])

def test_search():
    assert search([1,1,2,2,3]) == [3]
    assert search([1,2,3,4,5]) == [1,5]
    print("All tests passed")

if __name__ == "__main__":
    test_search()



def search2(l):
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l[0]
    if l[0] != l[1]:
        return l[0]
    if l[-1] != l[-2]:
        return l[-1]
    mid = len(l) // 2
    if l[mid] != l[mid-1]:
        return l[mid]
    else:
        return search(l[:mid])

def test_search():
    assert search([1,1,2,2,3]) == [3]
    assert search([1,2,3,4,5]) == [1,5]
    print("All tests passed")

if __name__ == "__main__":
    test_search()



def