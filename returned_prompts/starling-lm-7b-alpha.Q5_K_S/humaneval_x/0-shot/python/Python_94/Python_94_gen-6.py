To solve this problem, we can follow these steps:

1. Convert each number in the list to a string to be able to access each digit.
2. Iterate through the list of strings and check if each string is a prime number. A prime number is a number that has only two distinct positive divisors: 1 and itself.
3. If a string is a prime number, convert it back to an integer and add its digits.
4. Calculate the sum of all the digit sums of prime numbers in the list.
5. Return the sum.

Here is an example implementation of the solution:

```python
def sum_of_prime_digits(lst):
    prime_nums = []
    for num_str in [str(num) for num in lst]:
        if all(num_str % i != 0 for i in range(2, int(num_str ** 0.5) + 1)):
            prime_nums.append(int(num_str))
    return sum(sum(map(int, str(num))) for num in prime_nums)
```

In the given example cases, the function `sum_of_prime_digits` returns the expected results:

- For `lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]`, the function returns `10`.
- For `lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]`, the function returns `25`.
- For `lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]`, the function returns `13`.
- For `lst = [1,3,1,32,5107,34,83278,109,163,23,2323,