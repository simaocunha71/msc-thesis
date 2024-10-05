```
def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
        if len(result) == n - 1:
            break
    return result
```


In this solution, we define a helper function `is_prime` to check whether a number is prime or not. We then iterate from 2 to `n-1` and check each number to see if it's prime. If it is, we add it to the result list. We stop once we have `n-1` prime numbers in the list. Finally, we return the result list. 

Note that we don't need to check numbers greater than `n` because we're looking for prime numbers less than `n`. Also, we start the range from 2 because 0 and 1 are not prime numbers. 

This solution has a time complexity of O(n * sqrt(n)) because we're iterating up to `n` and for each number, we're doing a sqrt operation to check if it's prime. The space complexity is O(n) because we're storing the result in a list. 