    count := 0
    for i := 1; i <= 9; i++ {
        count += 1
    }
    for i := 1; i < 10**(n-1); i++ {
        count += 1
    }
    for i := 10**(n-1); i < 10**n; i++ {
        count += 1
    }
    return count
}