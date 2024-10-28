    count := 0
    for i := 2; a > 1; i++ {
        for a % i == 0 {
            a = a / i
            count++
        }
    }
    return count == 3
}



