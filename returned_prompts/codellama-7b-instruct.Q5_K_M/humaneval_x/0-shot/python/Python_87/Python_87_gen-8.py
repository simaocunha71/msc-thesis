
    def get_row(lst, x):
        lst = sorted(lst, key=lambda y: y.count(x))
        return [(i, lst[i].index(x)) for i in range(len(lst)) if x in lst[i]]