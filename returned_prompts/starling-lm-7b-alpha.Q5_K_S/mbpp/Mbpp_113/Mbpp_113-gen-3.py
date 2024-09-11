"""
Here is a function that checks if a string represents an integer or not.

"""

def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Test Cases
print(check_integer("python")) # False
print(check_integer("123"))  # True
print(check_integer("123.45")) # False
print(check_integer("123abc")) # False
print(check_integer("+123")) # False
print(check_integer("-123")) # False
print(check_integer("123x")) # False

# Expected Output
# False
# True
# False
# False
# False
# False
# False

```  


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  