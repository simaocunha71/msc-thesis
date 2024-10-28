func Tri(n int) []float64 {
    if n < 0 {
        return nil
    }
    if n == 0 {
        return []float64{3}
    }
    if n == 1 {
        return []float64{1, 3}
    }
    if n == 2 {
        return []float64{1, 3, 2}
    }
    if n == 3 {
        return []float64{1, 3, 2, 8}
    }
    result := make([]float64, n+1)
    result[0] = 1
    result[1] = 3
    result[2] = 2
    result[3] = 8
    for i := 4; i <= n; i++ {
        if i%2 == 0 {
            result[i] = 1 + float64(i)/2
        } else {
            result[i] = result[i-1] + result[i-2] + result[i-3]
        }
    }
    return result
}