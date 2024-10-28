    def get_row(lst, x):
        result = []
        for i, row in enumerate(lst):
            if x in row:
                result.append((i, row.index(x)))

        result.sort(key=lambda tup: tup[0])
        for tup in result:
            tup[1] = len(row) - tup[1] - 1
        result.sort(key=lambda tup: tup[1], reverse=True)
        return result


