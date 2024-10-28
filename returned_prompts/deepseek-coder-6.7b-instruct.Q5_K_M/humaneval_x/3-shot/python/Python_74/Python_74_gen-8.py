    def count_chars(lst):
        return sum(len(s) for s in lst)

    return lst1 if count_chars(lst1) < count_chars(lst2) else lst2

