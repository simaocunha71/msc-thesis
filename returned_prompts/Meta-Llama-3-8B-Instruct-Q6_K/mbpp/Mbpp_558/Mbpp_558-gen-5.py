```
def digit_distance_nums(num1, num2):
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    
    distance = 0
    for i in range(len(str(max_num))):
        if i >= len(str(min_num)):
            break
        distance += abs(int(str(max_num)[i]) - int(str(min_num)[i]))
    
    return distance
```


Explanation:
The task is to write a function that calculates the sum of the per-digit difference between two integers. For example, if the two integers are 1 and 2, the per-digit difference is 1 (the difference between the single digit 1 and 2), and the sum of this difference is 1.

The solution to this problem is to first find the maximum and minimum of the two numbers. Then, iterate over the digits of the maximum number, and for each digit, find the corresponding digit in the minimum number. If the minimum number does not have a digit at the current position, break the loop. Calculate the absolute difference between the two digits and add it to the total distance. Finally, return the total distance.

The unit test `assert digit_distance_nums(1,2) == 1` helps to clarify the problem by providing an example of the expected output for a given input. This test shows that the function should return 1 when the input is 1 and 2, which is the sum of the per-digit difference between these two numbers.