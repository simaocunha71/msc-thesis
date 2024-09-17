```
def digit_distance_nums(num1, num2):
    total_distance = 0
    max_digits = max(len(str(num1)), len(str(num2)))
    for i in range(max_digits):
        digit1 = str(num1)[:-1*i-1][::-1][i] if i < len(str(num1)) else '0'
        digit2 = str(num2)[:-1*i-1][::-1][i] if i < len(str(num2)) else '0'
        total_distance += abs(int(digit1) - int(digit2))
    return total_distance
```
This function works by first determining the maximum number of digits between the two input numbers. It then iterates over each digit position, using the string manipulation functions to extract the digit from each number. If a number has fewer digits than the maximum, it assumes that the missing digits are zero. The absolute difference between the two digits is then added to the total distance. The function returns the total distance. 

The unit test `assert digit_distance_nums(1,2) == 1` is used to verify that the function works correctly. It checks that the distance between the numbers 1 and 2 is 1, which is the sum of the absolute difference between their digits (0-1). 