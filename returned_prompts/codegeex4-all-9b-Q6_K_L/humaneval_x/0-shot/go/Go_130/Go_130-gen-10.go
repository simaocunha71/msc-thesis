func Tri(n int) []float64 {
    t := make([]float64, n+1)
    t[0] = 1
    t[1] = 3
    for i := 2; i <= n; i++ {
        if i%2 == 0 {
            t[i] = 1 + float64(i)/2
        } else {
            t[i] = t[i-1] + t[i-2] + t[i+1]
        }
    }
    return t
}