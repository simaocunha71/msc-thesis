def sum_even_and_even_index(lst):
    sum = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum

print(sum_even_and_even_index([5, 6, 12, 1, 18, 8]))  # Output: 30

"""
This program works by iterating over the list with a step of 2 (thus only accessing every other element, which are at even positions). It then checks if the current element is even by checking if the remainder of its division by 2 is 0. If it is, it adds it to the sum. The sum is then returned.
"""
<jupyter_output>
30
<jupyter_text>
Question 2
<jupyter_code>
