
def check_tuplex(tuplex, elem):
    if elem in tuplex:
        return True
    else:
        return False

print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r'))

# Output: True

# Alternatively, you can use the in keyword directly in Python:

def check_tuplex(tuplex, elem):
    return elem in tuplex

print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r'))

# Output: True
<jupyter_output>
True
True
<jupyter_text>
Problem 4
<jupyter_code>
