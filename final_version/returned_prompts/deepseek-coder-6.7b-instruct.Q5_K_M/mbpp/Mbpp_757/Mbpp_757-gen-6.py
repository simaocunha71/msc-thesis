"""
To solve this problem we need to iterate over the list and for each string check if its reverse is present in the list. 
"""

def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i][::-1] in lst:
            count += 1
    return count//2

assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2

#The double division is to avoid counting each pair twice (since each pair includes two strings and the check for a reverse string starts from the next index), so we divide by 2 at the end.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
