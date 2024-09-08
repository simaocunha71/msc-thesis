def find_substring(lst, sub):
    return any(sub in s for s in lst)

print(find_substring(["red", "black", "white", "green", "orange"],"ack"))

# True

"""
The function find_substring takes a list of strings and a substring as arguments. It uses the built-in any() function and a generator comprehension to check if the substring is in any of the strings in the list. If it is, it returns True; otherwise, it returns False.
"""
<jupyter_output>
True
<jupyter_text>
Question 2
<jupyter_code>
