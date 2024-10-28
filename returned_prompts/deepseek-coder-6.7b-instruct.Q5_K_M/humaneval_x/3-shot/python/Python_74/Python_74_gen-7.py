    def total_match(lst1, lst2):
        lst1_len = sum([len(i) for i in lst1])
        lst2_len = sum([len(i) for i in lst2])
        return lst1 if lst1_len < lst2_len else lst2


