    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            return append([]int{i}, Factorize(n / i)