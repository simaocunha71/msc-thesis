	for i, v := range arr {
		if v%2 == 0 {
			return []int{v, i}
		}
	}
	return []int{}
}