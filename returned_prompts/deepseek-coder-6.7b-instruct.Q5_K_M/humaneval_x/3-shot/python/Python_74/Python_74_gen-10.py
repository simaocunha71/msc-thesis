    def total_match(lst1, lst2):
        lst1_count = sum(len(i) for i in lst1)
        lst2_count = sum(len(i) for i in lst2)

        if lst1_count < lst2_count:
            return lst1
        else:
            return lst2


