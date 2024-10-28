	for i, num := range arr {
		if i == k {
			break A
		}
		if num > 9 {
			return -1
		}
	}

	sum := 0
	for _, num := range arr[:k] {
		sum += num
	}

	return sum
}