def find_substring(lst,sub):
    return any(sub in i for i in lst)

print(find_substring(["red", "black", "white", "green", "orange"],"ack"))

"""
The function find_substring takes a list and a substring as input. It uses the built-in any() function in python, which returns True if at least one element of an iterable is true. We are passing a generator to any() which checks if the substring is present in each string in the list.
"""
<jupyter_output>
True
<jupyter_text>
Question 2
<jupyter_code>
