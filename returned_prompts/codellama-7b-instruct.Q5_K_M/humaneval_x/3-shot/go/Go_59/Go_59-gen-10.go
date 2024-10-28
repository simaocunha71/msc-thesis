    for i := int(math.Sqrt(float64(n))) ; i > 1 ; i-- {
        if n % i == 0 {
            return i
        }
    }
    return n
}



