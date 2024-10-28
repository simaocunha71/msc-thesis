
	for i, v := range l {
		for j := i + 1; j < len(l); j++ {
			for k := j + 1; k < len(l); k++ {
				if v+l[j]+l[k] == 0 {
					return true
				}
			}
		}
	}

	return false
}
