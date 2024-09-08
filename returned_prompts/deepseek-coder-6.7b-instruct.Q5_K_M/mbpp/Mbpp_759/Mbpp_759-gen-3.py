def is_decimal(s):
    try:
        float(s)
    except ValueError:
        return False
    return s.count('.') == 1 and len(s.split('.')[1]) == 2

print(is_decimal('123.11'))  # True

"""
Explanation:
This function first tries to convert the given string to a float. If the conversion fails, it returns False. If the conversion is successful, it checks the string for a single decimal point and ensures that exactly two digits follow it. If all these conditions are met, it returns True.
"""
<jupyter_output>
True
<jupyter_text>
Question 2:
<jupyter_code>
