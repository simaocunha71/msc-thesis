    for i := 2; i < int(math.Sqrt(float64(x))); i++ {
        if x%i == 0 {
            return false
        }
    }
    return x != 1
}



