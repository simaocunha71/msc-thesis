    result := 0
    buckets := make([][]int,len(grid))
    for i:=0;i<len(grid);i++ {
        buckets[i] = make([]int,len(grid[i]))
    }
    for i:=0;i<len(grid);i++ {
        for j:=0;j<len(grid[i]);j++ {
            buckets[i][j] = grid[i][j] % capacity
        }
    }
    for i:=0;i<len(buckets);i++ {
        for j:=0;j<len(buckets[i]);j++ {
            result += buckets[i][j]
        }
    }
    return result / capacity
}



