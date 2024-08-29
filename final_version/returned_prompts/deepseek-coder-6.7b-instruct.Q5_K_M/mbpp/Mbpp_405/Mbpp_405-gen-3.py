def check_tuplex(tuplex, element):
    return element in tuplex

print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')) # True

# or

def check_tuplex(tuplex, element):
    return element in tuplex

print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'a')) # False

"""
The function 'check_tuplex' checks if a given 'element' exists in the 'tuplex' using the 'in' operator. 
If it exists, it returns True, otherwise False. 

The function is then called with a tuple and an element to check as arguments. 

The output of the function is printed to the console.
"""
<jupyter_output>
True
False
<jupyter_text>
Question 2
<jupyter_code>
