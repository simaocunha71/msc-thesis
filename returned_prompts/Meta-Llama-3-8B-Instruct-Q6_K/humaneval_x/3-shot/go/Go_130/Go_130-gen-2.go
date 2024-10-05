    if n == 0 {
        return []float64{}
    }
    if n == 1 {
        return []float64{3.0}
    }
    if n == 2 {
        return []float64{3.0, 2.0}
    }
    tri := make([]float64, n+1)
    tri[0] = 1.0
    tri[1] = 3.0
    tri[2] = 2.0
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            tri[i] = 1.0 + float64(i)/2.0
        } else {
            tri[i] = tri[i-1] + tri[i-2] + tri[i-3]
        }
    }
    return tri
}