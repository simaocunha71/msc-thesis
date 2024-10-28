    if n < 2 {
        return false
    }
    for i := 2; i < int(math.Sqrt(float64(n))) + 1; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}



