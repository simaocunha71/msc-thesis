
	for i, x := range lst1 {
		for j, y := range lst2 {
			if x == y {
				lst1[i] = y
				lst2[j] = x
				goto A
			}
		}
	}

	for _, x := range lst1 {
		if x%2 != 0 {
			return "NO"
		}
	}

	return "YES"
}
