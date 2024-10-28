```
def three_equal(a, b, c):
    count = 0
    if a == b and a == c:
        count = 3
    elif a == b or a == c or b == c:
        count = 2
    return count
```


Test:
```
assert test_three_equal(1,1,1) == 3
```


Explanation:
The function `three_equal(a, b, c)` takes three integers as input and counts the number of equal numbers among them. If all three numbers are equal, it returns 3. If two numbers are equal, it returns 2. If all numbers are different, it returns 0. The unit test `assert test_three_equal(1,1,1) == 3` ensures that the function works correctly when all three numbers are equal. 





```
def test_three_equal(a, b, c):
    return three_equal(a, b, c)
```





```
def three_equal(a, b, c):
    count = 0
    if a == b and a == c:
        count = 3
    elif a == b or a == c or b == c:
        count = 2
    return count
```





```
assert test_three_equal(1,1,1) == 3
```





```
assert test_three_equal(1,2,3) == 0
```





```
assert test_three_equal(1,1,2) == 2
```





```
assert test_three_equal(1,2,2) == 2
```





```
assert test_three_equal(1,1,1,2) == "Input should contain exactly three numbers"
```





```
def test_three_equal(a, b, c):
    if len([a, b, c]) != 3:
        return "Input should contain exactly three numbers"
    return three_equal(a, b, c)
```





```
assert test_three_equal(1,1,1) == 3
```





```
assert test_three_equal(1,2,3) == 0
```





```
assert test_three_equal(1,1,2) == 2
```





```
assert test_three_equal(1,2,2) == 2
```





```
assert test_three_equal(1,1,1,2) == "Input should contain exactly three numbers"
```





``