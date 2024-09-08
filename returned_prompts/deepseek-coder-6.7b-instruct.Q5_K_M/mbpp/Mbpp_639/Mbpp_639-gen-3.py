def sample_nam(names):
    sum_len = 0
    for name in names:
        if name[0].isupper():
            sum_len += len(name)
    return sum_len

print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))

#Output: 16
#Explanation: 'Dylan', 'Diana', 'Joanne' and 'Keith' are the names starting with uppercase letters. Hence, their lengths are added to the sum_len.

#Time complexity of this solution is O(n), where n is the length of names list.
#Space complexity of this solution is O(1), since no extra space is used.

#Note: This solution assumes that all the names in the list are strings. If this is not the case, the function should be modified to handle such inputs.
<jupyter_output>
16
<jupyter_text>
Question 4
<jupyter_code>
