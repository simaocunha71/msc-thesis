def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        if all(digit != 0 and num % digit == 0 for digit in map(int, str(num))):
            result.append(num)
    return result

print(divisible_by_digits(1,22))

"""
This function works by iterating over all numbers in the range from startnum to endnum. For each number, it converts it to a string, then maps that string to a list of its digits. It checks if every digit is non-zero and if the number is divisible by that digit. If it passes both checks, the number is appended to the result list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2
<jupyter_code>
