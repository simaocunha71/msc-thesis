    var (
        M       = len(grid)
        N       = len(grid[0])
        Q       = [][]int{}
        D       = make([][]int, M)
        V       = make([][]bool, M)
        minPath = []int{}
    )

    // 初始化
    for i := 0; i < M; i++ {
        D[i] = make([]int, N)
        V[i] = make([]bool, N)
    }

    // 初始化队列
    for i := 0; i < M; i++ {
        for j := 0; j < N; j++ {
            Q = append(Q, []int{i, j})
        }
    }

    // 迷宫遍历
    for i := 0; i < M*N; i++ {
        for i < len(Q) {
            // 弹出队列
            p := Q[0]
            Q = Q[1:]

            x, y := p[0], p[1]
            // 找到最短路径
            if D[x][y] == k {
                minPath = append(minPath, grid[x][y])
                goto A
            }

            // 上
            if x > 0 && !V[x-1][y] {
                V[x-1][y] = true
                D[x-1][y] = D[x][y] + 1
                Q = append(Q, []int{x - 1, y})
            }
            // 下
            if x < M-1 && !V[x+1][y] {
                V[x+1][y] = true
                D[x+1][y] = D[x][y] + 1
                Q = append(Q, []int{x + 1, y})
            }
            // 左
            if y > 0 && !V[x][y-1] {
                V[x][y-1] = true
                D[x][y-1] = D[x][y] + 1
                Q = append(Q, []int{x, y - 1})
            }
            // 右
            if y < N-1 && !V[x][y+1] {
                V[x][y+1] = true
                D[x][y+1] = D[x][y] + 1
                Q = append(Q, []int{x