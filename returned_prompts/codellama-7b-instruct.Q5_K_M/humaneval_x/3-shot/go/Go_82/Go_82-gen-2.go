    length := len(s)
    if length == 1 {
        return true
    }
    for i := 2; i < math.Sqrt(float64(length)); i++ {
        if length % i == 0 {
            return false
        }
    }
    return true
}



