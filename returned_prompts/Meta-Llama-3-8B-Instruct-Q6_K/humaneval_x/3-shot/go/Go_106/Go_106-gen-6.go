    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            var fact int = 1
            for j := 1; j <= i; j++ {
                fact *= j
            }
            result[i] = fact
        } else {
            var sum int = 0
            for j := 1; j <= i; j++ {
                sum += j
            }
            result[i] = sum
        }
    }
    return result
}