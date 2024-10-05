
	for i := 0; i < len(l); i++ {
		for j := 0; j < len(l); j++ {
			if l[i] == l[j] {
				continue A
			}
			if l[i]+l[j] == 0 {
				return true
			}
		}
	}
	return false
}
