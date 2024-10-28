
	if n < 0 {
		return -1
	}
	result := 1
	for i := n; i > 0; i-- {
		result *= i
	}
	return result
}
