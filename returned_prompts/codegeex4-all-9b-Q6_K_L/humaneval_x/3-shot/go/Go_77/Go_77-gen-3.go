    if a == 0 {
        return true
    }
    for i := -100; i < 100; i++ {
        if math.Pow(float64(i), 3) == float64(a) {
            return true
        }
    }
    return false
}



