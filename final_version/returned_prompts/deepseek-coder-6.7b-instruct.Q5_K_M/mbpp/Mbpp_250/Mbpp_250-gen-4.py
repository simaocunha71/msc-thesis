
def count_X(t, element):
    return t.count(element)

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4))

# OUTPUT:
# 0

# Explanation:
# The element 4 is not present in the tuple. Therefore, the function returns 0.

# IMPORTANT NOTE:
# This function will only work if the elements of the tuple are hashable. For example, it will not work if the tuple includes lists or dictionaries.
<jupyter_output>
0
<jupyter_text>
