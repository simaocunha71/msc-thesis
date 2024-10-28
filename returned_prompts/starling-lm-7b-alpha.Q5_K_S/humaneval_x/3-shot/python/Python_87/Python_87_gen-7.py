    def get_row(lst, x):
        # Initialize result list
        result = []
        # Iterate through the 2d list
        for i, row in enumerate(lst):
            # If the element exists in the current row, append the coordinate to the result
            if x in row:
                result.append((i, row.index(x)))

        # Sort the result by ascending row index
        result.sort(key=lambda tup: tup[0])
        # Sort the result by descending column index
        result.sort(key=lambda tup: tup[1], reverse=True)

        return result


