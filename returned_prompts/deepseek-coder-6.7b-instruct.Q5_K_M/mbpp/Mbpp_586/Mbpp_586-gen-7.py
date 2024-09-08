def split_Arr(arr, n):
    return arr[n:] + arr[:n]

# Test
print(split_Arr([12,10,5,6,52,36],2))
<jupyter_output>
[5, 6, 52, 36, 12, 10]
<jupyter_text>
2. Write a Python function that will take a list of numbers and return a dictionary with keys from the list and values as the square of the keys.For example, if you pass [1, 2, 3, 4, 5] to the function, it should return {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
<jupyter_code>
def square_dict(lst):
    return {i: i**2 for i in lst}

# Test
print(square_dict([1, 2, 3, 4, 5]))
<jupyter_output>
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
<jupyter_text>
3. Write a Python function that will take a list of numbers and return a new list with unique elements of the first list.
<jupyter_code>
def unique_list(lst):
    return list(set(lst))

# Test
print(unique_list([1, 2, 2, 3, 4, 4, 5, 6, 6, 7]))
<jupyter_output>
[1, 2, 3, 4, 5, 6, 7]
<jupyter_text>
4. Write a Python function that will take a list of strings and return a new list with only the strings that start with the letter 'a' or 'A'.
<jupyter_code>
def filter_strings(lst):
    return [s for s in lst if s[0].lower() == 'a']

# Test
print(filter_