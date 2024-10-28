    def largest_smallest_integers(lst):
        if not lst:
            return None, None

        neg_num = max(filter(lambda x: x < 0, lst))
        pos_num = min(filter(lambda x: x > 0, lst))

        return neg_num, pos_num


