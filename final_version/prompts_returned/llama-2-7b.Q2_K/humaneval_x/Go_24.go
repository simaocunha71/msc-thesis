
// For a given number n, find the largest number that divides n evenly, smaller than n
// >>> LargestDivisor(15)
// 5
func LargestDivisor(n int) int {
	if n < 2 {
		return 1
	}

	var ret = 0
	for i := int(1); i*i <= n; i += 1 {
		if n%i == 0 {
			ret = max(int(i), ret)
			break
		}
	}
	return ret
}
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}