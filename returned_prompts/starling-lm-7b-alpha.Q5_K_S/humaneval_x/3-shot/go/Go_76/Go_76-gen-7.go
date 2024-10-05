    for i := 0; i <= 30; i++ {
        if math.Pow(float64(n),float64(i)) == float64(x) {
            return true
        }
    }
    return false
}



