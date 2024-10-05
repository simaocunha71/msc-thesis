```python

def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and all(int(digit) % 2 == 1 for digit in str(num)[0] + str(num)[-1]):
            count += 1
    return count
```
