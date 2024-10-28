```
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        if all(int(digit) in str(num) and num % int(digit) == 0 for digit in str(num)):
            result.append(num)
    return result
```
This function works by iterating over the range from startnum to endnum (inclusive). For each number, it checks if the number is divisible by every digit it contains. It does this by converting the number to a string, iterating over each character (digit) in the string, and checking if the digit is present in the number and if the number is divisible by the digit. If the number meets these conditions, it is added to the result list. Finally, the function returns the result list. 

The unit test `assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]` ensures that the function is working correctly. It checks that the function returns the expected list of numbers when given the range from 1 to 22. 

The time complexity of this function is O(n*m), where n is the range from startnum to endnum and m is the maximum number of digits in the numbers in that range. This is because for each number in the range, the function checks every digit in the number. The space complexity is O(n), where n is the number of numbers in the range that meet the condition, because the function stores these numbers in a list. 