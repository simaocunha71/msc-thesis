"""
def check_distinct(t):
    return len(t) == len(set(t))

print(check_distinct((1, 4, 5, 6, 1, 4)))
"""


# Python3 program to check if a tuple contains duplicate
# elements or not

def check_distinct(t):
    # Convert tuple to set and compare length
    if(len(t) == len(set(t))):
        return True
    else:
        return False

# Driver code
print(check_distinct((1, 4, 5, 6, 1, 4)))
```