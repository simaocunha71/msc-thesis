    count := 0
    for i := 1; i <= 9; i++ {
        if i == 1 {
            count++
        }
        for j := 1; j <= 10^n-1; j *= 10 {
            if j%10 == 1 {
                count++
            }
        }
    }
    return count
}