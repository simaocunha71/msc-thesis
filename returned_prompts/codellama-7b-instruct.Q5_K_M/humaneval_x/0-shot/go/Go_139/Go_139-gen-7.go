
// The factorial is calculated by multiplying the given integer by the previous
// factorial minus one.
	result := 1
	for i := 1; i <= n; i++ {
		result = result * (n - i)
	}
	return result
}