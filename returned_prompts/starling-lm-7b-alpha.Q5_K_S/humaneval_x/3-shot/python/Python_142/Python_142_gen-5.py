    def squares_cubes(lst):
        for i in range(len(lst)):
            if i % 3 == 0:
                lst[i] *= lst[i]
            if i % 4 == 0 and i % 3 != 0:
                lst[i] *= lst[i] * lst[i]
        return sum(lst)


