```
def odd_num_sum(n):
    return sum(i**4 for i in range(1, 2*n+1, 2))
``` 
The function takes an integer `n` as input and returns the sum of fourth power of first `n` odd natural numbers. The unit test `assert odd_num_sum(2) == 82` helps to clarify the problem, as it indicates that the function should return the sum of the fourth powers of the first two odd natural numbers (1, 3). 

The solution uses a generator expression to generate the sequence of odd numbers up to `2*n+1`, and then sums up the fourth power of each number in this sequence. The `range` function is used with a step size of 2 to generate the sequence of odd numbers. The `sum` function is used to calculate the sum of the fourth powers of these numbers. 

For example, `odd_num_sum(2)` returns `1**4 + 3**4 = 1 + 81 = 82`, which matches the expected result. 

This solution has a time complexity of O(n) and a space complexity of O(1), as it only requires a constant amount of space to store the sum and the current number, regardless of the size of the input `n`. 