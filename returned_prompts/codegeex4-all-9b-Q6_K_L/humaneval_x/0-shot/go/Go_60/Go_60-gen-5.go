func SumToN(n int) int {
	if n == 1 {
		return 1
	}
	return n + SumToN(n-1)
}