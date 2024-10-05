def largest_smallest_integers(lst):
    positive_integers = [num for num in lst if num > 0]
    negative_integers = [num for num in lst if num < 0]
    return (max(negative_integers) if negative_integers else None,
            min(positive_integers) if positive_integers else None)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)