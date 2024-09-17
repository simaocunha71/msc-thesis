
def maxAverageOfPath(matrix: list) -> float:
    def helper(start, end):
        if start == end:
            return matrix[start[0]][start[1]]
        left = start[1] + 1
        right = start[1] - 1
        top = start[0] + 1
        bottom = start[0] - 1
        left_avg = helper((start[0], left), end)
        right_avg = helper((start[0], right), end)
        top_avg = helper((top, start[1]), end)
        bottom_avg = helper((bottom, start[1]), end)
        avg = (
            matrix[start[0]][start[1]]
            + matrix[end[0]][end[1]]
            + left_avg
            + right_avg
            + top_avg
            + bottom_avg
        ) / 5.0
        return avg

    return helper((0, 0), (len(matrix) - 1, len(matrix[0]) - 1))

