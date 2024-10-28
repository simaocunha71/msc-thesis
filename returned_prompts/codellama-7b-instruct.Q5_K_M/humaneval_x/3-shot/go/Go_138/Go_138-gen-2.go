    for i := 2; i <= int(math.Sqrt(float64(n))); i += 2 {
        if n == i {
            return false
        }
        for j := i + 2; j <= int(math.Sqrt(float64(n))); j += 2 {
            if n == i + j {
                return true
            }
        }
    }
    return false
}



