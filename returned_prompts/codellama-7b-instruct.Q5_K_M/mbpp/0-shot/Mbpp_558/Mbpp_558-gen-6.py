```python
def digit_distance_nums(num1, num2):
    num1_list = list(str(num1))
    num2_list = list(str(num2))
    result = 0
    for i in range(len(num1_list)):
        result += abs(int(num1_list[i]) - int(num2_list[i]))
    return result
```
