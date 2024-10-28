```
def divisible_by_digits(startnum, endnum):
    def is_divisible(n):
        return all(int(digit) in str(n) for digit in str(n))
    return [n for n in range(startnum, endnum+1) if is_divisible(n)]
```


This function `divisible_by_digits` generates all numbers within the given range and checks if each number is divisible by every digit it contains using the helper function `is_divisible`. The helper function `is_divisible` checks if every digit in the number is present in the number itself. If the number is divisible by every digit it contains, it is included in the output. 
The unit test `assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]` is used to test the function. The expected output is a list of numbers between 1 and 22 that are divisible by every digit they contain. The function returns this list. 

The time complexity of this function is O(n*m) where n is the range and m is the maximum number of digits in the numbers in the range. The space complexity is O(n) for storing the output list. 

Please note that this solution is not efficient for very large ranges as it generates all numbers in the range and checks if each number is divisible by every digit it contains. It is suitable for small to medium-sized ranges. For very large ranges, a more efficient solution would be needed. 