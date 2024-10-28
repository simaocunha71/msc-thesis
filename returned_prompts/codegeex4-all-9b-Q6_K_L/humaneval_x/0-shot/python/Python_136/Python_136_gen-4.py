def largest_smallest_integers(lst):
    negative = max(lst, default=None)
    positive = min(lst, default=None)
    negative = None if negative >= 0 else negative
    positive = None if positive <= 0 else positive
    return (negative, positive)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))