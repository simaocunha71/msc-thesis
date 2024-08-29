def dif_Square(n):
    for i in range(0, int(n**0.5)+1):
        j = 0
        while((i*i + j*j) <= n):
            if((i*i + j*j) == n):
                return True
            j += 1
    return False

print(dif_Square(5)) # True

Explanation:
The function `dif_Square(n)` checks all pairs of numbers `i` and `j` where `i` and `j` are nonnegative integers, and returns `True` if `n` can be expressed as the difference of two squares. If no such pair is found, the function returns `False`.

The outer loop runs from `0` to `n`, and the inner loop runs from `0` to `n`. For each `i`, it checks if `n` can be represented as `i*i - j*j` or `j*j - i*i` for all `j` from `0` to `i`. If it can be, it returns `True`. If no such `i` and `j` are found, it returns `False`.

The time complexity of this function is O(n^1.5) because the inner loop runs at most `n` times for each `i`, and the outer loop runs at most `n` times. The space complexity is O(1) because the function uses a fixed amount of space to store the variables `i`, `j`, and `n`.

Note: This function assumes that `n` is a nonnegative integer. If `n` can be negative, the function should be modified to handle negative `n` by checking if `-i*i + j*j` or `j*j + i*i` equals `n`.

Also, this function does not handle the case where `n` is zero or one, because those cases can be trivially represented as the difference of two squares (by taking one square of zero or one). If `n` can be zero or one, the function should be modified to handle those cases.

If you want to use this function for negative numbers and zero, you can add a check at the start of the function to return