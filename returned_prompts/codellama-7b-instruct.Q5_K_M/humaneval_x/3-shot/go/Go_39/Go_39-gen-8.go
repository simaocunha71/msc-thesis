    for i := 0; i < n; i++ {
        var a, b int = 0, 1
        for j := 0; j < i; j++ {
            a, b = b, a+b
            if math.Sqrt(float64(a*a + b*b)) == int(math.Sqrt(float64(a*a + b*b))) {
                return a
            }
        }
    }
    return 1
}



