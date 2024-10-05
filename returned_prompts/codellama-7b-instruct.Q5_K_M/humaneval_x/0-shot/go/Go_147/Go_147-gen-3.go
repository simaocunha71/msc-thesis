
	for i := 1; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				if i*i+j*j+k*k%3 == 0 {
					return 1
				}
			}
		}
	}
	return 0
}
