import re

def check_str(s):
    if re.match(r'^[aeiou]', s, re.IGNORECASE):
        return True
    else:
        return False

print(check_str("annie"))
print(check_str("Bannie"))
print(check_str("cannie"))
print(check_str("Dannie"))
print(check_str("Eannie"))
print(check_str("fannie"))

# Output:
# True
# False
# False
# False
# True
# False
<jupyter_output>
True
False
False
False
True
False
<jupyter_text>
