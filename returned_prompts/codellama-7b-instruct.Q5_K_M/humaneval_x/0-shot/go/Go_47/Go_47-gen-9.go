	sort.Ints(l)
	n := len(l)
	if n == 0 {
		return 0
	}
	if n%2 == 0 {
		return float64(l[n/2-1]+l[n/2]) / 2
	}
	return float64(l[n/2])
}
