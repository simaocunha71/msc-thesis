
    def max_fill(grid, capacity):
        import math
        def row_max_fill(row, capacity):
            # Find the max number of water that can be filled
            # in this row
            row_max = 0
            for j in range(len(row)):
                if row[j] == 1:
                    row_max += 1
                    if row_max == capacity:
                        break
            return row_max

        # Find the max number of water that can be filled
        # in each row
        max_fill = [row_max_fill(row, capacity) for row in grid]
        # Find the max number of water that can be filled
        # in the entire grid
        max_fill = max(max_fill)
        # Find the number of times we need to lower the bucket
        # to fill the grid
        return math.ceil(max_fill/capacity)

    def max_fill_opt(grid, capacity):
        import math
        def row_max_fill(row, capacity):
            row_max = 0
            for j in range(len(row)):
                if row[j] == 1:
                    row_max += 1
                    if row_max == capacity:
                        break
            return row_max

        max_fill = [row_max_fill(row, capacity) for row in grid]
        max_fill = max(max_fill)
        return math.ceil(max_fill/capacity)

    def max_fill_opt2(grid, capacity):
        import math
        def row_max_fill(row, capacity):
            row_max = 0
            for j in range(len(row)):
                if row[j] == 1:
                    row_max += 1
                    if row_max == capacity:
                        break
            return row_max

        max_fill = [row_max_fill(row, capacity) for row in grid]
        max_fill = max(max_fill)
        return int(math.ceil(max_fill/capacity))

    def max_fill_opt3(grid, capacity):
