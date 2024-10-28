    tri := make([]float64, n+2)
    tri[0] = 1
    tri[1] = 3
    tri[2] = 2
    for i := 3; i <= n+1; i++ {
        if i%2 == 0 {
            tri[i] = 1 + float64(i)/2
        } else {
            tri[i] = tri[i-1] + tri[i-