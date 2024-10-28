    result := make([]int, n)
    for i := 1; i <= n; i++ {
        if i % 2 == 0 {
            result[i-1] = math.Factorial(i)
        } else {
            result[i-1] = Sum(i)
        }
    }
    return result
}



