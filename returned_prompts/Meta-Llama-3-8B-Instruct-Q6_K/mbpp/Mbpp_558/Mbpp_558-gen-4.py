```
def digit_distance_nums(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        return "Input should be integers"
    sum_distance = 0
    while num1 or num2:
        digit1 = num1 % 10
        digit2 = num2 % 10
        sum_distance += abs(digit1 - digit2)
        num1 //= 10
        num2 //= 10
    return sum_distance
``` 
This function takes two integers as input, calculates the absolute difference between each pair of digits, and returns the sum of these differences. It handles the case where the input integers are not valid by returning an error message. The function uses the modulus operator `%` to extract the last digit of each number, and the floor division operator `//` to remove the last digit from each number. The process is repeated until both numbers are 0. The absolute difference between each pair of digits is calculated using the `abs` function and added to the `sum_distance` variable. The function returns the final value of `sum_distance`. 

For example, the function `digit_distance_nums(1,2)` returns `1` because the difference between the digits of 1 and 2 is 1 (|1-2|=1). The function works for any pair of integers, including those with different numbers of digits. 

The unit test `assert digit_distance_nums(1,2) == 1` ensures that the function returns the correct result for the input (1,2). This test helps to verify that the function is working correctly. 

The time complexity of this function is O(log(max(num1, num2))), where max(num1, num2) is the maximum number of digits in the input integers. This is because the function processes each digit of the input integers once. The space complexity is O(1), which means the function uses a constant amount of space, because it only uses a fixed number of variables to store the input integers and the sum of the differences. 