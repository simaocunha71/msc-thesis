    var result int
    sum := 0
    for i := 1; i <= n; i++ {
        a := i * i - i + 1
        sum += a
        if sum % 3 == 0 {
            result++
        }
    }
    return result
}