    count := 0
    for i := 1; i < 10; i++ {
        count += 1
        if i != 1 {
            for j := 0; j < n-1; j++ {
                count += 1
            }
        }
    }
    return count
}