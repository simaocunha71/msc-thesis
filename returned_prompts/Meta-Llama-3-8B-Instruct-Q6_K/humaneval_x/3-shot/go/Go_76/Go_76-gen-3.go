    for i := 1; ; i++ {
        if math.Pow(float64(n), float64(i)) == float64(x) {
            return true
        }
        if math.Pow(float64(n), float64(i)) > float64(x) {
            return false
        }
    }
}