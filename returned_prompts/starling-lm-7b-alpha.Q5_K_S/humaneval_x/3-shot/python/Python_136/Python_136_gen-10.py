    def largest_smallest_integers(lst):
        max_n = None
        min_n = None
        for n in lst:
            if n < 0 and (max_n is None or n > max_n):
                max_n = n
            if n > 0 and (min_n is None or n < min_n):
                min_n = n
        return max_n, min_n


