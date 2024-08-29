def square_nums(lst):
    return [i**2 for i in lst]

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# OUTPUT: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Explanation:
# The function square_nums takes in a list lst. It uses a list comprehension to iterate over each element in lst. For each element, it squares it (i**2) and adds it to a new list. The new list is then returned.
<jupyter_output>
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
<jupyter_text>
Q3. Write a function to find the sum of all elements in a list.
<jupyter_code>
