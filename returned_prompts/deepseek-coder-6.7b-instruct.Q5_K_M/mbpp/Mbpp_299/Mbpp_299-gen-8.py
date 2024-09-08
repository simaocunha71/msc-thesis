def max_aggregate(lst):
    d = {}
    for name, num in lst:
        if name in d:
            d[name] += num
        else:
            d[name] = num
    return max(d.items(), key=lambda x: x[1])

print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))

# Output: ('Juan Whelan', 212)

This function works by first creating a dictionary where the keys are the names and the values are the total aggregate values. Then, it returns the key-value pair with the maximum value. The lambda function is used to specify the key to be used for comparison in the max function.

"""
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""

"""
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""

"""
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""
<jupyter_output>
('Juan Whelan', 212)
<jupyter_text>
