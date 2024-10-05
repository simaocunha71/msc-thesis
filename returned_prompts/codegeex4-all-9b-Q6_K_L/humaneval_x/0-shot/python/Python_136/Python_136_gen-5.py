def largest_smallest_integers(lst):
    negative_integers = sorted([i for i in lst if i < 0])
    positive_integers = sorted([i for i in lst if i > 0])
    return (negative_integers[-1] if negative_integers else None,
            positive_integers[0] if positive_integers else None)