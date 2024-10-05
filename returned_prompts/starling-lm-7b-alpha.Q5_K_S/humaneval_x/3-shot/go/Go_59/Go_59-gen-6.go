    if n%2 == 0 {
        return 2
    }
    i := 3
    for i <= int(math.Sqrt(float64(n))) {
        if n%i == 0 {
            return LargestPrimeFactor(n/i)
        }
        i += 2
    }
    return n
}



