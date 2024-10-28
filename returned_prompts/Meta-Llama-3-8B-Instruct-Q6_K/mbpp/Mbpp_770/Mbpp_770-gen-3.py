```
def odd_num_sum(n):
    return sum(i**4 for i in range(1, 2*n+1, 2))
```
Explanation:
The function `odd_num_sum` takes an integer `n` as input and returns the sum of the fourth power of the first `n` odd natural numbers.

The unit test `assert odd_num_sum(2) == 82` helps to clarify the problem by providing an example of the expected output. This test suggests that the function should return the sum of the fourth power of the first 2 odd natural numbers, which are 1^4 + 3^4 = 1 + 81 = 82.

The solution uses a generator expression to calculate the fourth power of each odd number in the range from 1 to 2*n+1 with a step of 2. The `sum` function is then used to calculate the sum of these fourth powers. This approach ensures that only the odd numbers are considered and the sum is calculated correctly.