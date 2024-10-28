	if n == 1 {
		return nil
	}

	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		for n%i == 0 {
			n /= i
		}
		if n == 1 {
			goto A
		}
	}

	return []int{n}
}
