    def largest_smallest_integers(lst):
        negatives = [x for x in lst if x < 0]
        positives = [x for x in lst if x > 0]
        
        if negatives:
            largest_negative = max(negatives)
        else:
            largest_negative = None
        
        if positives:
            smallest_positive = min(positives)
        else:
            smallest_positive = None
        
        return (largest_negative, smallest_positive)
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
    print(largest_smallest_integers([]))  # Output: (None, None)
    print(largest_smallest_integers([0]))  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None)  # Output: (None, None) 