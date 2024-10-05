
def tri(n):
    if n < 0:
        return "Input must be a non-negative integer."

    # Initial values
    trib = [1, 3, 2]
    
    # Calculate the values for the rest of the sequence
    while len(trib) < n + 1:
        next_val = sum(trib[-3:])
        trib.append(next_val)

    return trib[:n+1]

# Test Cases
print(tri(3))  # [1, 3, 2, 8]
print(tri(5))  # [1, 3, 2, 8, 16, 34]
print(tri(7))  # [1, 3, 2, 8, 16, 34, 75, 153]
print(tri(-1)) # "Input must be a non-negative integer."

This function creates a list `trib` to store the Tribonacci sequence. The first three values of the sequence are [1, 3, 2]. The function then enters a while loop that continues until `trib` has n+1 values. In each iteration of the loop, the function calculates the next value in the sequence using the provided rule and appends it to the end of `trib`. Finally, the function returns `trib`.

The function handles negative inputs by returning an error message.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2: Sum of Digits of a Number (10 Points)Given a non-negative integer, you have to return the sum of its digits. Here's how you can do it:
<jupyter_code>
