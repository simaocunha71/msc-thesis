    if n % 2 == 0 {
        return y
    }
    i := 3
    for i <= math.Sqrt(float64(n)) {
        if n % i == 0 {
            return y
        }
        i += 2
    }
    return x
}



