
    def max_fill(grid, capacity):
        # count the number of 1s in each row
        rows = [sum(row) for row in grid]
        # sort the rows in descending order
        rows.sort(reverse=True)
        # initialize the number of times the buckets need to be lowered
        times = 0
        # initialize the total number of 1s in the grid
        total = sum(rows)
        # while there are still 1s in the grid
        while total > 0:
            # lower the buckets by one
            times += 1
            # for each row in the grid
            for i in range(len(rows)):
                # if the row has 1s left
                if rows[i] > 0:
                    # lower the bucket and decrement the count of 1s in the row
                    rows[i] -= 1
                    # decrement the total count of 1s in the grid
                    total -= 1
                # if the row has no 1s left
                else:
                    # skip to the next row
                    continue
                # if the count of 1s in the row is less than or equal to the bucket capacity
                if rows[i] <= capacity:
                    # lower the bucket and decrement the count of 1s in the row
                    rows[i] -= 1
                    # decrement the total count of 1s in the grid
                    total -= 1
                # if the count of 1s in the row is greater than the bucket capacity
                else:
                    # break the loop since the buckets can't be lowered further
                    break
        # return the number of times the buckets need to be lowered
        return times


print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)) # Output: 6
print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)) # Output: 5
print(max_fill([[0,0,0], [0,0,0]],