def find_substring(lst, substr):
    for word in lst:
        if substr in word:
            return True
    return False

print(find_substring(["red", "black", "white", "green", "orange"],"ack"))

"""
In the above function, we iterate over each word in the list and check if the substring is present in the word using the 'in' keyword. If we find a match, we return True. If we have checked all the words in the list and haven't found a match, we return False.
"""

# Output:
# True
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2
<jupyter_code>
