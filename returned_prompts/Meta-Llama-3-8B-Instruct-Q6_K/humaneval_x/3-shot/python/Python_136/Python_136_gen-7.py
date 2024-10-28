    def largest_smallest_integers(lst):
        negative_integers = [i for i in lst if isinstance(i, int) and i < 0]
        positive_integers = [i for i in lst if isinstance(i, int) and i > 0]

        if negative_integers:
            largest_negative_integer = max(negative_integers)
        else:
            largest_negative_integer = None

        if positive_integers:
            smallest_positive_integer = min(positive_integers)
        else:
            smallest_positive_integer = None

        return largest_negative_integer, smallest_positive_integer


