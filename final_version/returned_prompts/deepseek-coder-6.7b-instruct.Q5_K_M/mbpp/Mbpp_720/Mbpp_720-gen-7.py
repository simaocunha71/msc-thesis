
def add_dict_to_tuple(t, d):
    t += (d,)
    return t

t = (4, 5, 6)
d = {"MSAM"  : 1, "is" : 2, "best"  : 3}

print(add_dict_to_tuple(t, d))  # Output: (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})

"""
Explanation:
The function takes a tuple and a dictionary as inputs. It adds the dictionary to the tuple using the += operator and returns the modified tuple.
"""
<jupyter_output>
(4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
<jupyter_text>
1.3 Python Tuple Operations
<jupyter_code>
# Python Tuple Operations

# Tuple Concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)  # Output: (1, 2, 3, 4, 5, 6)

# Tuple Replication
t = (1, 2, 3)
print(t * 3)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Tuple Membership
print(4 in (1, 2, 3, 4, 5))  # Output: True
print(7 not in (1, 2, 3, 4, 5))  # Output: True

# Tuple Indexing and Slicing
t = (1, 2, 3, 4, 5)
print(t[1])  # Output: 2
print(t[-1])  # Output: 5
print(t[1:4])  # Output: (2, 3, 4)

# Tuple Assignment
t = (1, 2, 3)
t1, t2,