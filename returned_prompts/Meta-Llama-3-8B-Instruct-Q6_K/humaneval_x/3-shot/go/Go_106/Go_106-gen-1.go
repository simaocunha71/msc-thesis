    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = factorial(i)
        } else {
            sum := 0
            for j := 1; j <= i; j++ {
                sum += j
            }
            result[i] = sum
        }
    }
    return result
}

func factorial(n int) int {
    if n == 0 {
        return 1
    } else {
        return n * factorial(n-1)
    }
}