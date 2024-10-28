	sort.Ints(l)
	len := len(l)
	if len == 0 {
		return 0
	}
	if len%2 == 0 {
		return float64(l[len/2])
	} else {
		return float64(l[(len-1)/2])
	}
}

