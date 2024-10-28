
	for i, v := range l {
		for j, w := range l {
			if i != j && v+w == 0 {
				return true
			}
		}
	}
	return false
}
