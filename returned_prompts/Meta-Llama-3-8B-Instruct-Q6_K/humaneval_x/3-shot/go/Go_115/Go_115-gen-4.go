    var count int
    for _, row := range grid {
        for _, cell := range row {
            if cell == 1 {
                count += capacity
            }
        }
    }
    return count
}  // This is not the correct solution. The task is to empty the wells and it seems that it's asking for the number of times you need to lower the buckets. I will try to solve it again. 



