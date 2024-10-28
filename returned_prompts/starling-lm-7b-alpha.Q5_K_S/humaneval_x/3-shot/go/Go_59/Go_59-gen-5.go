    for i := 2; i <= math.Sqrt(float64(n)); i++ {
        if n % i == 0 {
            for j := 2; j <= math.Sqrt(float64(i)); j++ {
                if i % j == 0 {
                    return j
                }
            }
            return i
        }
    }
    return n
}



