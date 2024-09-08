
def check_none(tup):
    if None in tup:
        return True
    else:
        return False

print(check_none((10, 4, 5, 6, None)))

# Output:
# True

# Explanation:
# The function 'check_none' takes a tuple as an argument. It uses the 'in' operator to check if there is a None value in the tuple. If it finds a None value, it returns True, otherwise it returns False.
# The test case checks the function with a tuple that includes a None value, so it should return True.
<jupyter_output>
True
<jupyter_text>
