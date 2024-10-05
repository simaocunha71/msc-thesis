    def get_row(lst, x):
        coords = []
        for i, row in enumerate(lst):
            if x in row:
                coords.append((i, row.index(x)))

        coords.sort(key=lambda coord: coord[0])
        for coord in coords:
            coord[1] = len(lst[coord[0]]) - 1 - coord[1]
        coords.sort(key=lambda coord: coord[1], reverse=True)
        return coords


