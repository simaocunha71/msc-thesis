    count := 0
    for i := 1; i <= 10^n - 1; i++ {
        if i < 10^n || i % 10 == 1 {
            count++
        }
    }
    return count
}