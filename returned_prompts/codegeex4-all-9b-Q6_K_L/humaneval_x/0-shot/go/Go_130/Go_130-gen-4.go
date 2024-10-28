func Tri(n int) []float64 {
	tri := make([]float64, n+1)
	tri[0] = 3
	for i := 1; i < n+1; i++ {
		if i%2 == 0 {
			tri[i] = 1 + float64(i)/2
		} else {
			tri[i] = tri[i-1] + tri[i-2] + tri[i+1]
		}
	}
	return tri
}