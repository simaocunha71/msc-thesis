    for i := 2; i <= int(math.Sqrt(float64(a))); i++ {
        if a%i == 0 {
            return false
        }
    }
    return true
}



