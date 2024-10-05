    def largest_smallest_integers(lst):
        max_neg = None
        min_pos = None
        for i in lst:
            if i < 0 and (max_neg == None or i > max_neg):
                max_neg = i

            if i > 0 and (min_pos == None or i < min_pos):
                min_pos = i

        return max_neg, min_pos


