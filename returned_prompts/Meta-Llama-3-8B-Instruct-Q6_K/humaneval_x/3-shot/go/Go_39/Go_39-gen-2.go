    a, b := 0, 1
    for i := 0; i < n; i++ {
        a, b = b, a+b
        if math.Mod(float64(b), 2) == 0 {
            b++
        }
        for j := 2; j <= int(math.Sqrt(float64(b))); j++ {
            if b%j == 0 {
                b++
                i--
                break
            }
        }
    }
    return int(b)
}