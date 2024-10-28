    if n == 1 {
        return false
    }
    if n == 2 {
        return true
    }
    if n%2 == 0 {
        return false
    }
    max := int(math.Sqrt(float64(n))) + 1
    for i := 3; i < max; i += 2 {
        if n%i == 0 {
            return false
        }
    }
    return true
}



