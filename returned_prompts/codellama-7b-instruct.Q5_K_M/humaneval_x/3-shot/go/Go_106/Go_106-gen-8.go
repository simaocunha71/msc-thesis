    result := make([]int, n)
    for i := 1; i < n; i++ {
        if i%2 == 0 {
            result[i] = Factorial(i)
        } else {
            result[i] = SumFrom1To(i)
        }
    }
    return result
}



