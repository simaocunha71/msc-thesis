
def closest_integer(value):
    val = float(value)
    if val >= 0:
        return int(val + 0.5)
    else:
        return int(val - 0.5)

print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))

'''
This function works by first converting the input string to a float. Then, it checks if the float is greater or equal to zero. If it is, it adds 0.5 before converting to int to round up. If it's less than zero, it subtracts 0.5 before converting to int to round down.
'''

# Q3. Write a Python code that converts a given string to lowercase and removes leading and trailing spaces.

