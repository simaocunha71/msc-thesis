    def largest_smallest_integers(lst):
        if len(lst) == 0:
            return None, None
        max_neg = None
        min_pos = None
        for elem in lst:
            if elem < 0:
                if max_neg is None or elem > max_neg:
                    max_neg = elem
            elif elem > 0:
                if min_pos is None or elem < min_pos:
                    min_pos = elem
        return max_neg, min_pos


