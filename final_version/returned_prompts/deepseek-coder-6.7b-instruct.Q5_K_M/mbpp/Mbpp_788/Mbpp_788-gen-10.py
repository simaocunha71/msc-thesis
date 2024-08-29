def new_tuple(str_list, str2):
    return tuple(str_list) + (str2,)

print(new_tuple(["WEB",  "is"], "best"))

# Output: ('WEB', 'is', 'best')

# Explanation:
# The function new_tuple takes a list and a string as input. It converts the list to a tuple using the tuple() function, 
# and then concatenates the tuple with the string using the + operator. The string is converted to a tuple by appending 
# a comma, which is necessary because the tuple function expects a comma-separated sequence of elements. 
# The result is a new tuple that includes all the elements of the input sequence.
<jupyter_output>
('WEB', 'is', 'best')
<jupyter_text>
Question 2:
<jupyter_code>
