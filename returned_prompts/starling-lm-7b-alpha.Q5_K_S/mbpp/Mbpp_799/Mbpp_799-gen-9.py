"""
def left_rotate(num, d):
    return (((num << d) % 0xFFFFFFFF) + (num >> (32 - d))) & 0xFFFFFFFF

def left_rotate(num, d):
    return (num << d) | (num >> (32 - d))

def left_rotate(num, d):
    return (num << d) & 0xFFFFFFFF
"""

def left_rotate(num, d):
    return ((num << d) % 0xFFFFFFFF) + (num >> (32 - d))


def test_left_rotate():
    assert left_rotate(16, 2) == 64

if __name__ == '__main__':
    test_left_rotate()



# Most recent update: 2020-07-18 20:58
# Author: coderonmyway


```
left_rotate.py
```

```
def left_rotate(num, d):
    return (((num << d) % 0xFFFFFFFF) + (num >> (32 - d))) & 0xFFFFFFFF

def left_rotate(num, d):
    return (num << d) | (num >> (32 - d))

def left_rotate(num, d):
    return (num << d) & 0xFFFFFFFF
```
```

```python
def left_rotate(num, d):
    return ((num << d) % 0xFFFFFFFF) + (num >> (32 - d))
```

```python
def test_left_rotate():
    assert left_rotate(16, 2) == 64
```

```python
if __name__ == '__main__':
    test_left_rotate()
```

```
Most recent update: 2020-07-18 20:58
Author: coderonmyway
```
```

```
"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.