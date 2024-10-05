Here is the Python code to solve the problem:

```Python
def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = []
    i = 2
    while i < n:
        if is_prime(i):
            result.append(i)
        i += 1
    return result
```
This function first defines a helper function `is_prime` to check whether a number is prime or not. Then it iterates from 2 to `n-1`, checks each number whether it is prime or not, and if it is, adds it to the result list. Finally, it returns the result list. 

Please note that this function is not optimized for large inputs because it checks every number whether it is prime or not. For large inputs, a more efficient algorithm is needed. 

Also note that this function returns an empty list if `n` is 0 or 1, as per the problem description. If you want to return `[2]` for `n=2` and an empty list for `n=0`, you can modify the function accordingly. 

The time complexity of this function is O(n sqrt(n)), where n is the input. The space complexity is O(n), where n is the number of prime numbers less than the input. 