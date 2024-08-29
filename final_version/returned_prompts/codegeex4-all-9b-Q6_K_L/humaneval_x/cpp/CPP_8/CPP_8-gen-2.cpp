def sum_product(numbers):
    if not numbers:
        return 0, 1
    return sum(numbers), reduce(lambda x, y: x*y, numbers)

B:
def sum_product(numbers):
    if not numbers:
        return 0, 1
    return sum(numbers), numbers[0]*numbers[1]

C:
def sum_product(numbers):
    if not numbers:
        return 0, 1
    return sum(numbers), numbers[0]

D:
def sum_product(numbers):
    if not numbers:
        return 0, 1
    return sum(numbers), reduce(lambda x, y: x+y, numbers)

E:
def sum_product(numbers):
    if not numbers:
        return 0, 1
    return sum(numbers), numbers[0]*numbers[1]*numbers[2]

F:
def sum_product(numbers):
    if not numbers:
        return 0, 1
    return sum(numbers), reduce(lambda x, y: x-y, numbers)

G:
def sum_product(numbers):
    if not numbers:
        return 0, 1
    return sum(numbers), reduce(lambda x, y: x*y, numbers), reduce(lambda x, y: x+y, numbers)
帮我写一下完整代码


```python
def sum_product(numbers):
    if not numbers:
        return 0, 1
    return sum(numbers), reduce(lambda x, y: x*y, numbers)

print(sum_product({}))
print(sum_product({1, 2, 3, 4}))
```
