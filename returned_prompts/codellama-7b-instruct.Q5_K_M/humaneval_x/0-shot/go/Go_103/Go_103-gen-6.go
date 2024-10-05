	if n > m {
		return -1
	}

	total := 0
	for i := n; i <= m; i++ {
		total += i
	}

	avg := total / (m - n + 1)
	return fmt.Sprintf("0b%b", int(math.Round(float64(avg))))
}
