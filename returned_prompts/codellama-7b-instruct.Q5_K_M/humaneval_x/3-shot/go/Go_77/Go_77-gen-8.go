    for i := 1; i < math.Sqrt(float64(a)); i++ {
        if math.Pow(float64(i), 3) == float64(a) {
            return true
        }
    }
    return false
}



