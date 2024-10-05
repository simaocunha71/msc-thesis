    def largest_smallest_integers(lst):
        negative = [x for x in lst if x < 0]
        positive = [x for x in lst if x > 0]

        if negative:
            largest_negative = max(negative)
        else:
            largest_negative = None

        if positive:
            smallest_positive = min(positive)
        else:
            smallest_positive = None

        return largest_negative, smallest_positive
    # You can test the function with the following code:
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
    print(largest_smallest_integers([]))  # Output: (None, None)
    print(largest_smallest_integers([0]))  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output