    factors := make([]int, 0)

    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            n /= i
            factors = append(factors, i)
            i--
        }
    }
    if n > 1 {
        factors = append(factors, n)
    }

    return factors
}



