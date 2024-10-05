    type tuple struct {
        int, int, int
    }

    var dp [][][]int = make([][][]int, len(grid))
    for i  := range dp  {
        dp[i] = make([][]int, len(grid[i]))
        for j  := range dp[i]  {
            dp[i][j] = make([]int, k+1)
            for l  := range dp[i][j]  {
                dp[i][j][l] = math.MaxInt32
            }
        }
    }

    var q []tuple = make([]tuple, 0)
    for i  := range grid  {
        for j  := range grid[i]  {
            q = append(q, tuple{i, j, grid[i][j]})
        }
    }

    var dir  []int = []int{-1, 0, 1, 0, -1}
    sort.Slice(q, func(i, j int) bool {
        return q[i].int < q[j].int
    })

    for len(q)  != 0  {
        var t tuple = q[0]
        q = q[1:]
        var x, y, v = t.int, t.int1, t.int2
        if dp[x][y][v]  < dp[t.int][t.int1][t.int2]  {
            continue
        }
        for i  := 0; i < 4; i++  {
            var nx, ny = x + dir[i], y + dir[i+1]
            if nx  != -1  && ny  != -1  && nx  != len(grid)  && ny  != len(grid[0])  && grid[nx][ny]  < v  {
                for l  := k; l >= v; l--  {
                    dp[nx][ny][l] = min(dp[nx][ny][l], dp[x][