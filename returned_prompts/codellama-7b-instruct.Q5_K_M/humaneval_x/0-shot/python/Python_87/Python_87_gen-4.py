
    def get_row(lst, x):
        row = []
        for i, l in enumerate(lst):
            for j, y in enumerate(l):
                if y == x:
                    row.append((i, j))
        row.sort(key=lambda x: x[0])
        for i in row:
            i[1] = len(lst[i[0]]) - i[1] - 1
        return row
    
    
    def get_row(lst, x):
        return [(i, len(l) - 1 - j) for i, l in enumerate(lst) for j, y in enumerate(l) if y == x]

