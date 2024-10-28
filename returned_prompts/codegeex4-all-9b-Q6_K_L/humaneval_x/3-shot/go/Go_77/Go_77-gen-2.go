    if a == 0 {
        return true
    }

    for i := 0; i <= math.Abs(float64(a)); i++ {
        if i*i*i == a {
            return true
        }
    }
    return false
}

