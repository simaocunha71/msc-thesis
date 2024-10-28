    result := make([]int, n)
    factorial := 1

    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            factorial *= i
            result[i] = factorial
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



