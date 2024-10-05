
    negative_numbers = [n for n in lst if n < 0]
    positive_numbers = [n for n in lst if n > 0]

    if not negative_numbers:
        largest_negative = None
    else:
        largest_negative = max(negative_numbers)

    if not positive_numbers:
        smallest_positive = None
    else:
        smallest_positive = min(positive_numbers)

    return (largest_negative, smallest_positive)

print(largest_smallest_integers([2, 4, -1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)


# The function above works by first creating two lists: one for negative numbers and one for positive numbers.
# Then it checks if there are any negative or positive numbers. If not, it sets the respective variable as None.
# If there are any, it finds the largest negative number and the smallest positive number.
# Finally, it returns a tuple with the largest negative and smallest positive number.
<jupyter_output>
(None, 1)
(None, None)
(None, None)
<jupyter_text>
Question 3
<jupyter_code>
