```
def sumofFactors(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum
```


Explanation:
The problem is asking to write a function that calculates the sum of all even factors of a given number. 

The function iterates from 1 to the given number and checks if the current number is a factor of the given number using the modulus operator. If it is, it checks if the factor is even by using the modulus operator again. If the factor is even, it adds it to the sum.

The unit test `assert sumofFactors(18) == 26` helps to understand the problem better. It means that the sum of even factors of 18 is 26, which is 2 + 6 + 9 + 18.

This function has a time complexity of O(n) because it iterates from 1 to n. It has a space complexity of O(1) because it uses a constant amount of space. 