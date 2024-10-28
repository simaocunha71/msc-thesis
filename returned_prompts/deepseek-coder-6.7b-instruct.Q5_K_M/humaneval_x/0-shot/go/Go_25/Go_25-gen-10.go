    var factors []int

    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            factors = append(factors, i)
            n = n / i
            i--
        }
    }

    if n != 1 {
        factors = append(factors, n)
    }

    return factors
}

