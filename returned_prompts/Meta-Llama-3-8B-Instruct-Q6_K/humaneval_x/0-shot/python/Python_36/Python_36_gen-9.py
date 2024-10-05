```
def fizz_buzz(n: int):
    count = 0
    for i in range(11, n, 11):
        if i % 13 == 0:
            count += str(i).count('7')
    for i in range(13, n, 13):
        if str(i).count('7') > 0:
            count += 1
    return count
```
This function counts the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. It does this by iterating over the range from 11 to n-1 in increments of 11, and for each number in this range, it checks if the number is also divisible by 13. If it is, it counts the number of 7s in the number. It does the same for the range from 13 to n-1 in increments of 13, but only counts the numbers that contain the digit 7. The total count is then returned.