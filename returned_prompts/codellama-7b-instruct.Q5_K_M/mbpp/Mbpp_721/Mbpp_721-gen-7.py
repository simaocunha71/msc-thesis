"""
def maxAverageOfPath(matrix):
    # Compute the sum of all cells and the number of cells
    total_sum, num_cells = 0, 0
    for row in matrix:
        for cell in row:
            total_sum += cell
            num_cells += 1

    # Compute the maximum possible average
    max_avg = total_sum / num_cells

    # Compute the maximum average of all possible paths
    max_path_avg = -1
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # If the cell is not the top-left corner
            if row > 0 or col > 0:
                # Compute the path cost and average
                path_cost = matrix[row][col]
                path_avg = path_cost / (num_cells - 1)

                # Update the maximum average
                max_path_avg = max(max_path_avg, path_avg)

    return max_path_avg
"""
