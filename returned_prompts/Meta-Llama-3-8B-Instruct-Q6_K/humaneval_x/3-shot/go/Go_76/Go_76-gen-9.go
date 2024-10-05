    if n == 1 {
        return false
    }
    base := int(math.Pow(float64(n), float64(int(math.Log(float64(x)) / math.Log(float64(n))))))
    return base == x
}