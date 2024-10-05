    # first, determine how many rows and columns we have
    # then, we can use a two-dimensional array to keep track of which wells are 
    # already filled, and which are not
    # then, we can use a loop to keep going through each well
    # we can use a modular arithmetic to determine where we are in the grid
    # and where we have to go
    # we can use a counter to keep track of the number of times we have to lower the buckets


class Solution(object):
    def max_fill(self, grid, capacity):
        rows, columns = len(grid), len(grid[0])
        filled = [[False for _ in range(columns)] for _ in range(rows)]
        counter = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1 and not filled[i][j]:
                    self.fill(grid, filled, i, j, rows, columns, capacity)
                    counter += 1
        return counter
    
    def fill(self, grid, filled, i, j, rows, columns, capacity):
        current_capacity = 0
        current_row = i
        current_column = j
        while current_row >= 0 and current_column < columns and not filled[current_row][current_column]:
            if grid[current_row][current_column] == 1:
                current_capacity += 1
            if current_capacity == capacity:
                filled[current_row][current_column] = True
                current_capacity = 0
            if current_row > 0:
                current_row -= 1
            else:
                current_column += 1
        if current_row < 0 and current_column >= columns and current_capacity < capacity:
            filled[0][current_column] = True
            current_capacity = 0
            current_row = 0
            current_column += 1
        while current_row < rows and current_column < columns and current_capacity < capacity:
            if grid[current_row][current_column] == 1:
                current_capacity += 