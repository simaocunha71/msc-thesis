```
def sumofFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum
```


Explanation:
The function sumofFactors takes an integer n as an argument and returns the sum of all even factors of n. It uses a for loop to iterate over all numbers from 1 to n (inclusive) and checks if the current number is a factor of n by using the modulus operator (%). If the current number is a factor of n, it checks if the current number is even by using the modulus operator again. If the current number is even, it adds it to the sum. Finally, it returns the sum of all even factors. The unit test `assert sumofFactors(18) == 26` ensures that the function works correctly.  For example, the factors of 18 are 1, 2, 3, 6, 9, and 18, and the sum of the even factors (2, 6, and 18) is 26.  The function correctly returns this sum.  



The function has a time complexity of O(n) because it needs to iterate over all numbers from 1 to n. The space complexity is O(1) because it uses a constant amount of space to store the sum.  This function can be optimized by only checking up to the square root of n for factors, as any factor larger than the square root of n would have a corresponding factor smaller than the square root of n.  However, this optimization is not necessary for the given problem.  



The function can also be written using list comprehension and the built-in sum function:
```
def sumofFactors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0 and i % 2 == 0)
```
This version of the function is more concise but has the same time and space complexity as the original function.  



Another way to optimize the function is to use a set to store the factors and then sum the even factors.  This can be done using the following function:
```
def sumofFactors(n):
    factors = {i for i in range(1, n + 1) if n % i == 0}
    return sum(i for i in factors if i % 2 ==