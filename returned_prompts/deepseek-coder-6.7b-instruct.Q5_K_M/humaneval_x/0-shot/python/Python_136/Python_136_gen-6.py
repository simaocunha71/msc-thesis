
    # initialize variables
    max_neg = None
    min_pos = None

    # iterate over the list
    for num in lst:
        # check if the number is negative and larger than the current max_neg
        if num < 0 and (max_neg is None or num > max_neg):
            max_neg = num

        # check if the number is positive and smaller than the current min_pos
        elif num > 0 and (min_pos is None or num < min_pos):
            min_pos = num

    return max_neg, min_pos

print(largest_smallest_integers([2, 4,_ 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))
print(largest_smallest_integers([-1, -2, -3, 1, 2, 3]))
print(largest_smallest_integers([-1, -2, -3, 0]))

This code is working by iterating over the input list, and checking each element to see if it is a negative integer larger than the current max_neg, and if it is a positive integer smaller than the current min_pos. If it is, then it updates the respective variable. Finally, it returns a tuple of the max_neg and min_pos variables. If no appropriate numbers were found, the respective variables remain as None.
<jupyter_output>
<empty_output>
<jupyter_text>
**Question 3**Given a string, write a function that returns the string in reverse order. For example, if the input string is 'hello world', the function should return 'dlrow olleh'.
<jupyter_code>
