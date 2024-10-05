    factors := make([]int, 0)

    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        for n % i == 0 {
            factors = append(factors, i)
            n = n / i
        }
    }

    if n > 1 {
        factors = append(factors, n)
    }

    return factors
}



