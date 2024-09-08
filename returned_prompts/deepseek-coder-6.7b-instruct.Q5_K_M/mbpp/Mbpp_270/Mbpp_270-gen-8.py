def sum_even_and_even_index(lst):
    return sum(x for i, x in enenumarate(lst) if i % 2 == 0 and x % 2 == 0)

print(sum_even_and_even_index([5, 6, 12, 1, 18, 8]))


# The function sum_even_and_even_index is using a generator expression to sum up even numbers at even indexes of the list.
# enumerate is used to get both index and value for each element in the list.
# The if condition checks if the index is even (i % 2 == 0) and the number itself is even (x % 2 == 0). If both conditions are true, the number is included in the sum.
# The function returns the sum of these numbers.
# The test case [5, 6, 12, 1, 18, 8] returns 30 because 6 (at index 1) and 12 (at index 2) are the only even numbers at even indexes. Their sum is 18.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
