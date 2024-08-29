
def overlapping(seq1, seq2):
    return any(item in seq1 for item in seq2)

print(overlapping([1,2,3,4,5],[6,7,8,9]))

# OUTPUT: False

"""
This function uses the built-in any() function to check if any item in the second sequence (seq2) is in the first sequence (seq1). 
If any item in seq2 is found in seq1, the function will return True, otherwise it will return False.
"""
<jupyter_output>
False
<jupyter_text>
Q2:
<jupyter_code>
