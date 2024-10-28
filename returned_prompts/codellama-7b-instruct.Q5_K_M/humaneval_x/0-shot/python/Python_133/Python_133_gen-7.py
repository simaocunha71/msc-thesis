
    def sum_squares(lst):
        for i in range(len(lst)):
            lst[i] = int(lst[i] + 1)
        result = sum(x**2 for x in lst)
        return result




