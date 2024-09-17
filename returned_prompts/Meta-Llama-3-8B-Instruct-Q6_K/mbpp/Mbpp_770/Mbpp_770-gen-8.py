```
def odd_num_sum(n):
    return sum(i**4 for i in range(1, 2*n+1, 2))
```
This function calculates the sum of the fourth power of the first n odd natural numbers. It uses a generator expression to generate the sequence of odd numbers and then sums them up using the built-in sum function. The range function is used to generate the sequence, with the third argument set to 2 to ensure that only odd numbers are generated. The expression i**4 calculates the fourth power of each number, which is then summed up. The function is tested with the input n=2, which returns the expected result of 82.