
	for i, v := range l {
		for j := range l {
			if i == j {
				continue
			}
			if v+l[j] == 0 {
				return true
			}
		}
	}
	return false
}
