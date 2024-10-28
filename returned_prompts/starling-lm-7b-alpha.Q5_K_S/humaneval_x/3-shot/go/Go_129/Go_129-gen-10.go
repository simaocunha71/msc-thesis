    N := len(grid)
    P := make([]int, 0)
    for i := 0; i < N; i++ {
        for j := 0; j < N; j++ {
            if k == 0 {
                return P
            }
            P = append(P, grid[i][j])
            k--
        }
    }
    return P
}



