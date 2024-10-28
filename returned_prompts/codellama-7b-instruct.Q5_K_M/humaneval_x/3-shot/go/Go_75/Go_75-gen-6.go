    if a <= 1 {
        return false
    }
    for i := 2; i < math.Sqrt(float64(a)); i++ {
        if a%i == 0 {
            return false
        }
    }
    return true
}



