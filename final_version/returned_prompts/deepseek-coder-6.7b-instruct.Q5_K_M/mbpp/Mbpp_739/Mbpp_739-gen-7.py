
def find_Index(n):
    i = 1
    while True:
        triangular_num = i*(i+1)//2
        if len(str(triangular_num)) == n:
            return i
        i += 1

print(find_Index(2)) # should return 4


"""
Explanation:

Triangular numbers are a sequence of numbers where each number is the sum of the previous numbers. 
For example, the 7th triangular number is 28. The sequence of triangular numbers starts: 1, 3, 6, 10, 15, 21, 28, ...

This function starts from the first triangular number (1) and adds one to the counter each time it finds a triangular number with n digits. 
When it finds such a number, it returns the counter value.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
