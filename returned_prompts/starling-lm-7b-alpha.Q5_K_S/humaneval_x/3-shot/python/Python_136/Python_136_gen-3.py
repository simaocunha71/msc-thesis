    def largest_smallest_integers(lst):
        if len(lst) == 0:
            return None, None

        max_negative = None
        min_positive = None

        for elem in lst:
            if elem < 0 and (max_negative is None or elem > max_negative):
                max_negative = elem

            if elem > 0 and (min_positive is None or elem < min_positive):
                min_positive = elem

        return max_negative, min_positive


