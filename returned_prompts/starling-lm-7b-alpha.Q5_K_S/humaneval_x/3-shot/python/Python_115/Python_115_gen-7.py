    def max_fill(grid, capacity):
        """
        Using a greedy algorithm, we start from the left most column of each row,
        and try to fill the bucket with maximum number of units, until the bucket is full,
        or all units in the current column are exhausted.

        We keep track of the number of buckets required to fill the grid, by initializing a counter.

        We also keep track of the maximum number of units we can fill in the current column,
        by initializing a counter.

        We initialize a counter for the total number of units filled in the grid.

        For each row in the grid, we do the following:
            While the current column has units left to be filled, and the bucket is not full:
                If the current unit is 1, we increase the counter of total units filled,
                and the counter of units to be filled in the current column.
                We also fill the bucket, by increasing the counter of filled buckets,
                and decreasing the counter of units to be filled in the current column.

                If the current unit is 0, we decrease the counter of units to be filled in the current column.

            We increase the counter of filled buckets, and move to the next column.

        We return the total number of filled buckets.
        """

        filled_buckets_counter = 0
        total_units_filled = 0
        buckets_filled_in_row = 0

        for row in grid:
            units_to_be_filled_in_column = len(row)
            bucket_filled_in_column = 0

            while units_to_be_filled_in_column > 0 and bucket_filled_in_column < capacity:
                if row[units_to_be_filled_in_column-1] == 1:
                    total_units_filled += 1
                    units_to_be_filled_in_column -= 1
                    bucket_filled_in_column += 1
                else:
                    units_to_be_filled_in_column -= 1

            filled_buckets_counter += 1
            buckets_filled