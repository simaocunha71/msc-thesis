"""
def find_Max_Num(digits):
    digits.sort(reverse=True)
    num = ""
    for i in digits:
        num += str(i)
    return int(num)
"""

def find_Max_Num(digits):
    digits.sort(reverse=True)
    num = ""
    for i in digits:
        num += str(i)
    return int(num)

def test_find_Max_Num():
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([1,2,2,3]) == 3221
    assert find_Max_Num([1,1,2,3]) == 3211
    assert find_Max_Num([0,0,0,0]) == 0000
    test_find_Max_Num()

test_find_Max_Num()





















"""
def find_Max_Num(digits):
    digits.sort(reverse=True)
    num = ""
    for i in digits:
        num += str(i)
    return int(num)

def test_find_Max_Num():
    assert find_Max_Num([1,2,3]) == 321
    assert find_Max_Num([1,2,2,3]) == 3221
    assert find_Max_Num([1,1,2,3]) == 3211
    assert find_Max_Num([0,0,0,0]) == 0000
    test_find_Max_Num()

test_find_Max_Num()
"""

```

```
def find_Max_Num(digits):
    digits.sort(reverse=True)
    num = ""
    for i in digits:
        num += str(i)
    return int(num)

def test_find_Max_Num():
    assert find_Max_Num([1,2,3]) == 321
    assert find