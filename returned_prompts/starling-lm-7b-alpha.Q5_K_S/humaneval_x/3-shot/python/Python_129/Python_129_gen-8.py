    def get_neighbors(grid, i, j):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[i]):
                neighbors.append((i + dx, j + dy))
        return neighbors

    def is_valid_move(grid, i, j, k, visited_cells):
        neighbors = get_neighbors(grid, i, j)
        for idx, neighbor in enumerate(neighbors):
            if (neighbor not in visited_cells) and (grid[neighbor[0]][neighbor[1]] not in values):
                if idx == 0:
                    return (neighbor, grid[neighbor[0]][neighbor[1]])
                else:
                    return (neighbor, grid[neighbor[0]][neighbor[1]], neighbors[idx + 1])
        return None

    def find_next_cell(grid, i, j, k, visited_cells, values):
        if k == 1:
            return (i, j)
        valid_move = is_valid_move(grid, i, j, k, visited_cells)
        if valid_move:
            if valid_move[0] not in visited_cells:
                visited_cells.add(valid_move[0])
                values.append(valid_move[1])
                if valid_move[2] is None:
                    return valid_move[0]
                else:
                    return find_next_cell(grid, valid_move[2][0], valid_move[2][1], k - 2, visited_cells, values)
            else:
                return find_next_cell(grid, valid_move[0], valid_move[1], k - 2, visited_cells, values)
        else:
            return None

    def find_min_path(grid, k):
        values =