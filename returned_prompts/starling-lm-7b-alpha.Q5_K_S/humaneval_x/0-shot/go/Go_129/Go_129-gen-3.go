
// This is a brute force solution that tries all possible paths of length k.
// It is not suitable for large input sizes.

func minpath(grid [][]int, k, i, j, n int, p []int) []int {
    if k == 0 {
        return p[:]
    }
    if i >= n || i < 0 || j >= n || j < 0 {
        return p[:]
    }
    for _, v := range [][]int{{i + 1, j}, {i - 1, j}, {i, j + 1}, {i, j - 1}} {
        p[k-1] = grid[v[0]][v[1]]
        r := minpath(grid, k-1, v[0], v[1], n, p)
        if r != nil {
            return append(p[:k-1], r...)
        }
    }
    return nil
}

    if k == 0 {
        return []int{}
    }
    if k == 1 {
        return grid[0]
    }

    n := len(grid)
    p := make([]int, k)
    p[0] = grid[0][0]
    r := minpath(grid, k-1, 0, 0, n, p)
    if r != nil {
        return append(p[:1], r...)
    }
    return nil
}

// Time complexity: O(N^2 * (N^2)^(k/2))
// Space complexity: O(k)

// This is a modified version of the above brute force solution that tries all
// possible paths of length k, but only keeps the best path found so far.
// It is not suitable for large input sizes.

func minpath(grid [][]int, k, i, j, n int, p []int) []int {
    if k == 0 {
        return p[:]
    }
    if i >= n || i < 0 || j >= n || j < 0 {
        return p[:]
    }
    for _, v := range [][]int{{i + 1, j}, {