```
def sum(a, b):
    def find_divisors(n):
        return [i for i in range(1, n+1) if n % i == 0]

    divisors_a = find_divisors(a)
    divisors_b = find_divisors(b)

    common_divisors = [i for i in divisors_a if i in divisors_b]
    return sum(common_divisors)
```


The problem is asking for a function that takes two numbers as input and returns the sum of their common divisors. 

The provided unit test `assert sum(10,15) == 6` helps to understand the problem better. It indicates that the function should return 6 when given 10 and 15 as input, which are the common divisors 1, 2, 5.

The solution involves first defining a helper function `find_divisors` to find all divisors of a given number. Then, we find all common divisors by taking the intersection of the divisors of the two numbers. Finally, we return the sum of these common divisors. 

In the given solution, the `find_divisors` function uses a list comprehension to generate a list of all numbers from 1 to the given number that divide the number evenly. The main function uses this helper function to find the divisors of the two input numbers, then finds the common divisors by taking the intersection of these two lists. The sum of the common divisors is then returned. 

This solution has a time complexity of O(n), where n is the maximum of the two input numbers, because it needs to iterate up to the maximum of the two numbers to find all divisors. 

The provided unit test `assert sum(10,15) == 6` helps to ensure that the function is working correctly by testing it with specific input values. 

Note: The provided unit test is not exhaustive and the function may not work correctly for all possible input values. It is always a good practice to write more unit tests to cover all possible scenarios and edge cases. 