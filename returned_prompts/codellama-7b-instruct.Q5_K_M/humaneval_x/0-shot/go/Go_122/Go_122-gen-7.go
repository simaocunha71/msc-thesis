	for i := range arr {
		if i == k {
			break A
		}
		for j := range arr {
			if j == i {
				continue
			}
			for l := range arr {
				if l == j || l == i {
					continue
				}
				if l == k {
					break
				}
				if j+1 == l {
					continue
				}
				return arr[i] + arr[j] + arr[l]
			}
		}
	}
	return 0
}


