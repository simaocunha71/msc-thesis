    // Find all the numbers from 1 to N*N that are not yet in the grid
    // and are not larger than k.
    // Then for each of those numbers, find the minimum path in the grid.

    available := make([]int, 0)
    for i := 1; i <= len(grid)*len(grid); i++ {
        if i > k {
            break
        }
        if i > len(grid) {
            available = append(available, i)
            continue
        }
        if grid[i/len(grid)][i%len(grid)] == 0 {
            available = append(available, i)
        }
    }

    min_path := make([]int, 0)
    min_length := math.MaxFloat64
    for _, number := range available {
        length, path := find_min_path(grid, number, k)
        if length < min_length {
            min_path = path
            min_length = length
        }
    }
    return min_path
}

func find_min_path(grid [][]int, number int, k int) (float64, []int) {
    // Find the cell with the given number
    i := number / len(grid)
    j := number % len(grid)

    // Try all the directions from the current cell
    paths := make(map[int][]int)
    for _, offset := range [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}} {
        new_i := i + offset[0]
        new_j := j + offset[1]
        if new_i >= 0 && new_j >= 0 && new_i < len(grid) && new_j < len(grid) {
            if grid[new_i][new_j] != 0 {
                continue
            }
            path := append([]int{number}, find_min_path(grid, grid[new_i][new_j], k-1)...)
            paths[number] = path
        }
    }

    // Sort all the paths by lexicographic order and