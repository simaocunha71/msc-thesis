    if len(s) == 1{
        return true
    }

    for i := 2; i <= int(math.Sqrt(float64(len(s)))); i++ {
        if len(s) % i == 0 {
            return false
        }
    }
    return true
}



