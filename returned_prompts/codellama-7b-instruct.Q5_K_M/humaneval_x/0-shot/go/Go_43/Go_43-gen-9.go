
	for i := range l {
		for j := range l {
			if i == j {
				continue
			}
			if l[i] == -l[j] {
				return true
			}
		}
	}
	return false
}
