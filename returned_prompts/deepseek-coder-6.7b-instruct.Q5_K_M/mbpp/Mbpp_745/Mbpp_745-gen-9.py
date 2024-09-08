def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        digits = [int(i) for i in str(num)]
        if all(num % digit == 0 for digit in digits):
            result.append(num)
    return result

print(divisible_by_digits(1, 22))

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

# Time Complexity: O(n*m) where n is the range and m is the average number of digits in the numbers in the range.
# Space Complexity: O(n) where n is the range of numbers. In the worst case, all numbers in the range will be stored in the result list.
<jupyter_output>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
<jupyter_text>
**Q6. Given a list of integers, write a function to return the count of subarrays with a sum equal to a given number.**
<jupyter_code>
