	sort.Ints(l)
	size := len(l)
	if size%2 == 0 {
		return float64(l[size/2]+l[(size/2)-1]) / 2
	}
	return float64(l[size/2])
}
