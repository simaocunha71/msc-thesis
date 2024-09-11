```
def amicable_numbers_sum(n):
    amicable_numbers = [sum(divisors(i)) for i in range(1,n+1) if sum(divisors(i))!=i]
    return sum(amicable_numbers)

def divisors(n):
    if n%2==0:
        return [i for i in range(2,n+1,2)]
    else:
        return [i for i in range(3,n+1,2)]
```

In the above code, we first define a function `divisors(n)` which calculates all the divisors of `n` by iterating from 2 to `n` and adding the divisors to a list if the number is even, and from 3 to `n` if the number is odd.

Then, we define the `amicable_numbers_sum(n)` function, which calculates the sum of all amicable numbers from 1 to `n`. We create a list of amicable numbers by iterating from 1 to `n` and for each number, we check if the sum of its divisors is equal to the number itself. If not, we add the number to the list of amicable numbers. Finally, we return the sum of all amicable numbers.

To test the function, we can use the `assert` statement to check if the sum of amicable numbers calculated by the function is equal to the expected result (504 in this case).

Overall, this code provides a solution to calculate the sum of all amicable numbers from 1 to a specified number using Python.

Note: It's important to note that the `divisors(n)` function assumes that `n` is a positive integer greater than or equal to 2. If `n` is negative or less than 2, it may result in an error.
```

```
  
