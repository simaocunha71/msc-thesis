    for i := 0; i <= int(math.Cbrt(float64(a)))+1; i++ {
        if i * i * i == a {
            return true
        }
    }
    return false
}

