def sum_even_and_even_index(lst):
    sum = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum

print(sum_even_and_even_index([5, 6, 12, 1, 18, 8]))
<jupyter_output>
30
<jupyter_text>
Q3. Write a Python function to find the sum of squares of all numbers in a given list.
<jupyter_code>
