    length := len(s)
    for i := 2; i < int(math.Sqrt(float64(length))); i++ {
        if length%i == 0 {
            return false
        }
    }
    return true
}



