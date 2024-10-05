    for i  := 0; math.Pow(float64(n), float64(i)) <= float64(x); i++ {
        if math.Pow(float64(n), float64(i)) == float64(x) {
            return true
        }
    }
    return false
}


