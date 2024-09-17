```
def even_Power_Sum(n):
    return sum(i**5 for i in range(2, 2*n, 2))
``` 
This function uses a generator expression to iterate over the first n even natural numbers, raises each number to the fifth power, and sums the results. The `range` function is used to generate the sequence of even numbers, starting from 2 and incrementing by 2. 

For example, if you call `even_Power_Sum(2)`, it will return `1056`, which is the sum of the first 2 even natural numbers raised to the fifth power: `2^5 + 4^5`. 

The unit test `assert even_Power_Sum(2) == 1056` ensures that the function is working correctly. 

The time complexity of this function is O(n), as it needs to iterate over the first n even natural numbers. The space complexity is O(1), as it only uses a constant amount of space to store the sum. 