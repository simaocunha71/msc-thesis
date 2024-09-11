"""
def remove_odd(li):
    li1 = []
    for i in li:
        if i % 2 == 0:
            li1.append(i)
    return li1
"""

def remove_odd(li):
    return [i for i in li if i % 2 == 0]

def test_remove_odd():
    assert remove_odd([1,2,3]) == [2]
    print("All Test cases Passed")

test_remove_odd()

# Another Approach: Using list comprehension
"""
def remove_odd(li):
    return [i for i in li if i % 2 == 0]
"""

# Driver code

def remove_odd(li):
    return [i for i in li if i % 2 == 0]

def test_remove_odd():
    assert remove_odd([1,2,3]) == [2]
    print("All Test cases Passed")

test_remove_odd()

# This code contributed by
# Shubham Singh(SS17)

```
  
```
def remove_odd(li):
    li1 = []
    for i in li:
        if i % 2 == 0:
            li1.append(i)
    return li1
```
```

```
"""
def remove_odd(li):
    return [i for i in li if i % 2 == 0]
"""
```
```

```
def test_remove_odd():
    assert remove_odd([1,2,3]) == [2]
    print("All Test cases Passed")
```
```

```
def remove_odd(li):
    return [i for i in li if i % 2 == 0]
```
```

```
def test_remove_odd():
    assert remove_odd([1,2,3]) == [2]
    print("All Test cases Passed")
```
```
```
```