    def helper(lst):
        for idx, elem in enumerate(lst):
            if idx % 3 == 0:
                lst[idx] = lst[idx] ** 2
            elif idx % 4 == 0 and idx % 3 != 0:
                lst[idx] = lst[idx] ** 3
        return sum(lst)


