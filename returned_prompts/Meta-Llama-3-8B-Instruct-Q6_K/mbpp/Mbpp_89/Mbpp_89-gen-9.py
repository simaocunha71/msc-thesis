```
def closest_num(n):
    for i in range(n-1, -1, -1):
        if i < n:
            return i
    return -1
```


The function `closest_num` takes an integer `n` as input and returns the closest smaller number to `n`. If no smaller number is found, it returns `-1`.

The function iterates from `n-1` down to `1` (inclusive) and returns the first number it finds that is smaller than `n`. This ensures that the returned number is the closest smaller number to `n`.

For example, if `n` is `11`, the function will return `10`, which is the closest smaller number to `11`. If `n` is `0`, the function will return `-1`, because there is no smaller number than `0`. 

The unit test `assert closest_num(11) == 10` ensures that the function works correctly for the input `11`. 

The time complexity of this function is O(n), where n is the input number, because in the worst case it needs to iterate from `n-1` down to `1`. The space complexity is O(1), because it only uses a constant amount of space to store the function's variables and the loop's index. 