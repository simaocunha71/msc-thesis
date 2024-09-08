
def find_Index(n):
    i = 1
    while True:
        triangular_number = i*(i+1)//2
        if len(str(triangular_number)) == n:
            return i
        i += 1

# Test the function
print(find_Index(2))  # Should return 4

"""
Explanation:

The nth triangular number is given by the formula n*(n+1)/2. We start with i=1 and increment it until we find a triangular number with n digits. 
When we find such a number, we return the current value of i.
"""
<jupyter_output>
4
<jupyter_text>
Q2. Write a Python program to determine whether the given number is a Harshad number or not.
<jupyter_code>
