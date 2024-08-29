
import re

def check_str(word):
    if re.match(r'^[aeiou]', word):
        return True
    else:
        return False

print(check_str("annie"))  # Output: True
print(check_str("blu"))  # Output: False
<jupyter_output>
True
False
<jupyter_text>
Q2.
<jupyter_code>
