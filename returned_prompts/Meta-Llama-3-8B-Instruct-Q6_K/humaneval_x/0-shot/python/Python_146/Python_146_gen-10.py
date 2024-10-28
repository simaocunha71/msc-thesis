```
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and num % 10 % 2 != 0 and num // 10 % 10 % 2 != 0:
            count += 1
    return count
```



Explanation:

The function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and both first and last digits of a number are odd.

Here is the step by step breakdown of the function:

1. Initialize a counter variable `count` to 0. This variable will keep track of the number of elements that meet the condition.

2. Iterate over each number `num` in the input array `nums`.

3. Check if the number is greater than 10 using the condition `num > 10`.

4. Check if the last digit of the number is odd by taking the modulus of the number with 10 (`num % 10`) and then taking the modulus of the result with 2 (`num % 10 % 2`). If the result is not equal to 0, it means the last digit is odd.

5. Check if the first digit of the number is odd by taking the integer division of the number with 10 (`num // 10`), then taking the modulus of the result with 10 (`num // 10 % 10`) and then taking the modulus of the result with 2 (`num // 10 % 10 % 2`). If the result is not equal to 0, it means the first digit is odd.

6. If both conditions are met (i.e., the number is greater than 10 and both first and last digits are odd), increment the `count` variable by 1.

7. After iterating over all numbers in the array, return the `count` variable, which represents the number of elements that meet the condition.