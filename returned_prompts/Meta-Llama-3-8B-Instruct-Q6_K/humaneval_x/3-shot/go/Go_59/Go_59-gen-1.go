    max_factor := 0
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        for n % i == 0 {
            max_factor = i
            n /= i
        }
    }
    if n > max_factor {
        max_factor = n
    }
    return max_factor
}



