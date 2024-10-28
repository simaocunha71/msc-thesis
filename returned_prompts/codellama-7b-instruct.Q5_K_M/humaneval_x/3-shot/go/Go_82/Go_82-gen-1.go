    var length int = len(s)
    if length == 0 || length == 1 {
        return false
    }

    for i := 2; i < math.Sqrt(float64(length)); i++ {
        if length % i == 0 {
            return false
        }
    }
    return true
}



