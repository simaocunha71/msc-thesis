    def total_match(lst1, lst2):
        if sum(map(len, lst1)) < sum(map(len, lst2)):
            return lst1
        elif sum(map(len, lst1)) == sum(map(len, lst2)):
            return lst1
        else:
            return lst2

    return total_match(lst1, lst2)


