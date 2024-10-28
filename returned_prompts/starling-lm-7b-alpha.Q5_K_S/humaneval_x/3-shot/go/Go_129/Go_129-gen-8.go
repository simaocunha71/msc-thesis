    def check(x,y,n int) bool {
        return x >= 0 && x < n && y >= 0 && y < n
    }

    def solve(grid [][]int, n, k, cur_x, cur_y, path []int, min_path []int, cur_min_len int) {
        if len(path) == k {
            if cur_min_len < min_len {
                min_len = cur_min_len
                min_path = append(min_path, path...)
            }
        }else {
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                if check(cur_x+dx, cur_y+dy, n) {
                    path = append(path, grid[cur_x+dx][cur_y+dy])
                    solve(grid, n, k, cur_x+dx, cur_y+dy, path, min_path, cur_min_len+1)
                    path = path[:len(path)-1]
                }
        }
    }

    min_len := math.MaxInt32
    min_path := []int{}
    solve(grid, n, k, 0, 0, []int{}, min_path, min_len)
    return min_path
}



























































































































































































