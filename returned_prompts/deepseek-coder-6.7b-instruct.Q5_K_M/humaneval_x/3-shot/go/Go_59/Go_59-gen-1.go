    largest_factor := 2
    for n % 2 == 0 {
        n = n / 2
    }

    sqrt_n := int(math.Sqrt(float64(n)))
    for i := 3; i <= sqrt_n; i += 2 {
        while n % i == 0 {
            largest_factor = i
            n = n / i
        }
    }

    if n > 2 {
        largest_factor = n
    }

    return largest_factor
}



