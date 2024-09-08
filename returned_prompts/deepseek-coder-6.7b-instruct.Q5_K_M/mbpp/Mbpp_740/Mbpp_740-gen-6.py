
def tuple_to_dict(t):
    return {t[i]: t[i+1] for i in range(0, len(t)-1, 2)}

print(tuple_to_dict((1, 5, 7, 10, 13, 5)))

# Output: {1: 5, 7: 10, 13: 5}

# Explanation:
# The function iterates over the given tuple in steps of 2 (i.e., adjacent elements) and creates a dictionary where the current element is a key and the next one is a value.
# This way, it pairs up the elements of the given tuple as required.
<jupyter_output>
{1: 5, 7: 10, 13: 5}
<jupyter_text>
Question 2
<jupyter_code>
