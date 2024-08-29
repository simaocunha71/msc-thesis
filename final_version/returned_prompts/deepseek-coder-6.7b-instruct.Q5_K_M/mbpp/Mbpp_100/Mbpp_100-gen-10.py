def next_smallest_palindrome(num):
    while True:
        num += 1
        if str(num) == str(num)[::-1]:
            return num

print(next_smallest_palindrome(99))  # 101

"""
Explanation:
The function `next_smallest_palindrome` takes an integer `num` as input. It then increments `num` by 1 and checks if the string representation of the new number is the same as its reverse (which would make it a palindrome). If it is, it returns the number. If it isn't, it repeats the process with the new number.
"""
<jupyter_output>
101
<jupyter_text>
Question 2
<jupyter_code>
