    for i := 2; i <= int(math.Sqrt(float64(a))); i++ {
        for j := i; j <= int(math.Sqrt(float64(a))); j++ {
            for k := j; k <= int(math.Sqrt(float64(a))); k++ {
                if i * j * k == a {
                    return true
                }
            }
        }
    }
    return false
}