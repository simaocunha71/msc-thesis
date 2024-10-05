	for i, node := range arr {
		if node%2 == 0 {
			return []int{node, i}
		}
	}

	for i, node := range arr {
		if node%2 == 0 && node == math.MinInt32 {
			return []int{node, i}
		}
	}

	return []int{}
}

