    result := 0
    buckets := make([][]int, len(grid))
    for i := 0; i < len(buckets); i++ {
        buckets[i] = make([]int, len(grid[i]))
    }
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            buckets[i][j] = grid[i][j]
        }
    }

    for {
        result += 1
        for i := 0; i < len(buckets); i++ {
            for j := 0; j < len(buckets[i]); j++ {
                if buckets[i][j] == 1 {
                    buckets[i][j] -= 1
                    for i_ := 0; i_ < len(buckets); i_++ {
                        for j_ := 0; j_ < len(buckets[i_]); j_++ {
                            if buckets[i_][j_] == 1 {
                                buckets[i_][j_] -= 1
                            }
                        }
                    }
                }
            }
        }
        ok := true
        for i := 0; i < len(buckets); i++ {
            for j := 0; j < len(buckets[i]); j++ {
                if buckets[i][j] == 1 {
                    ok = false
                    break
                }
            }
        }
        if ok {
            break
        }
    }
    return result
}



