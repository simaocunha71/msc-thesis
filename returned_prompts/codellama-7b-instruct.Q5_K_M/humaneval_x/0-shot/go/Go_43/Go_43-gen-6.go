	for i := range l {
		for j := i + 1; j < len(l); j++ {
			if l[i] == -l[j] {
				return true
			}
		}
	}
	return false
}
