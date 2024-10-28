	for {
		if n == 1 {
			break A
		}
		if n%2 == 0 {
			n /= 2
		} else {
			n = 3*n + 1
		}
	}
	return []int{n}
}
