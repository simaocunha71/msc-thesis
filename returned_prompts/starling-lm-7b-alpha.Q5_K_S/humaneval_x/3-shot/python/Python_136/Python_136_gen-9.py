    def largest_smallest_integers(lst):
        if len(lst) == 0:
            return None, None
        neg_ints = [i for i in lst if i < 0]
        pos_ints = [i for i in lst if i > 0]
        if len(neg_ints) == 0:
            return None, min(pos_ints) if pos_ints else None
        elif len(pos_ints) == 0:
            return max(neg_ints) if neg_ints else None, None
        else:
            return max(neg_ints), min(pos_ints)


