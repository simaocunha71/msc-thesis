def remove_whitespaces(s):
    return s.replace(' ', '')

print(remove_whitespaces(' Google    Flutter '))  # GoogleFlutter

# Alternatively, you can use the join() and split() functions:
def remove_whitespaces(s):
    return ''.join(s.split())

print(remove_whitespaces(' Google    Flutter '))  # GoogleFlutter

# Alternatively, you can use a list comprehension:
def remove_whitespaces(s):
    return ''.join([char for char in s if not char.isspace()])

print(remove_whitespaces(' Google    Flutter '))  # GoogleFlutter
<jupyter_output>
GoogleFlutter
GoogleFlutter
GoogleFlutter
<jupyter_text>
Question 2
<jupyter_code>
