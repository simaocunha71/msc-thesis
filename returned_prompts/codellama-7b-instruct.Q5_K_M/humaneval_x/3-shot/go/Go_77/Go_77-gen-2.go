    for i := 1; i <= int(math.Sqrt(float64(a))); i++ {
        if a == i*i*i {
            return true
        }
    }
    return false
}



