    if x < 0 {
        return false
    }
    if n < 1 {
        return false
    }
    if x == 0 {
        return true
    }
    for i := int(math.Pow(float64(n), float64(0))); i <= x; i = int(math.Pow(float64(n), float64(i+1))) {
        if i == x {
            return true
        }
    }
    return false
}