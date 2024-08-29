
def odd_Equivalent(s, k):
    # Creating the equivalent binary strings
    bin_str = [s[i:] + s[:i] for i in range(len(s))]

    # Counting the odd binary strings
    odd_count = 0
    for i in bin_str:
        if int(i,2) % 2 == 1:
            odd_count +=1

    return odd_count

print(odd_Equivalent("011001",6))

#Output: 3


"""
Explanation:

The input string "011001" is rotated 6 times to get all possible rotations.
The rotated strings are:
"011001", "100110", "001100", "011001", "100110", "001100".

From these, only "011001", "100110" and "001100" have odd binary values. Hence, the answer is 3.
"""
<jupyter_output>
3
<jupyter_text>
Question 2
<jupyter_code>
