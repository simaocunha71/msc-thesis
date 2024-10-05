func Tri(n int) []float64 {
    seq := make([]float64, n+1)
    seq[0] = 3
    for i := 1; i <= n; i++ {
        if i%2 == 0 {
            seq[i] = 1 + float64(i)/2
        } else {
            seq[i] = seq[i-1] + seq[i-2] + seq[i+1]
        }
    }
    return seq
}