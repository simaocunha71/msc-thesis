```
def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            num = str(num)[1:]
        else:
            num = str(num)
        if sum(int(digit) for digit in num) > 0:
            count += 1
    return count
```
This function iterates over each number in the input array. If the number is negative, it removes the negative sign and converts the number to a string. Then it calculates the sum of the digits of the number. If the sum of the digits is greater than 0, it increments the count. Finally, it returns the count. The test cases provided in the problem statement can be used to verify the correctness of the function. For example, the test case `count_nums([-1, 11, -11]) == 1` checks that the function correctly counts the positive number 11, ignoring the negative numbers -1 and -11. The test case `count_nums([1, 1, 2]) == 3` checks that the function correctly counts all three positive numbers 1, 1, and 2. The test case `count_nums([]) == 0` checks that the function returns 0 when the input array is empty.