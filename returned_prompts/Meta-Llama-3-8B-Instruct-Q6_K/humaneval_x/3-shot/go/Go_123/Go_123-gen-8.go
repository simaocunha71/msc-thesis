    result := make([]int, 0)
    for n != 1 {
        if n % 2 == 1 {
            result = append(result, n)
            n = 3*n + 1
        } else {
            n = n / 2
        }
    }
    return result
}