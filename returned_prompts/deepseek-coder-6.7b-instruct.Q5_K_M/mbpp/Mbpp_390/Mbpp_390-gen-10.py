def add_string(lst, fmt):
    return [fmt.format(i) for i in lst]

print(add_string([1,2,3,4],'temp{0}'))

# Output: ['temp1', 'temp2', 'temp3', 'temp4']

# Explanation:
# The function `add_string` takes a list `lst` and a string `fmt`. It uses a list comprehension to iterate over each element in `lst`. The `format` method of the string is used to replace `{0}` with the element in `lst`. The resulting string is added to a new list which is returned.
# In the example, the list `[1,2,3,4]` and the string `'temp{0}'` are passed to the function. The function returns a new list where each element is the result of replacing `{0}` in `'temp{0}'` with the corresponding element in `[1,2,3,4]`.
<jupyter_output>
['temp1', 'temp2', 'temp3', 'temp4']
<jupyter_text>
Question 3
<jupyter_code>
