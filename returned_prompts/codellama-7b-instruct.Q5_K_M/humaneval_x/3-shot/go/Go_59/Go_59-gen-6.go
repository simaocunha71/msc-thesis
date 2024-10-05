    if n == 2 {
        return n
    }

    for i := 2; i < math.Sqrt(float64(n)); i++ {
        if n % i == 0 {
            return LargestPrimeFactor(i)
        }
    }
    return n
}



