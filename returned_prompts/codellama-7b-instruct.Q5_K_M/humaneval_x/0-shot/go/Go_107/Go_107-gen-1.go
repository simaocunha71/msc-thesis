	for i := 1; i <= n; i++ {
		if i == 1 {
			return [2]int{1, 1}
		}
		if i == 2 {
			return [2]int{1, 1}
		}
		if i == 3 {
			return [2]int{1, 2}
		}
		if i == 4 {
			return [2]int{2, 2}
		}
		if i == 5 {
			return [2]int{2, 3}
		}
		if i == 6 {
			return [2]int{3, 3}
		}
		if i == 7 {
			return [2]int{3, 4}
		}
		if i == 8 {
			return [2]int{4, 4}
		}
		if i == 9 {
			return [2]int{4, 5}
		}
		if i == 10 {
			return [2]int{5, 5}
		}
		if i == 11 {
			return [2]int{5, 6}
		}
		if i == 12 {
			return [2]int{6, 6}
		}
	}
	return [2]int{0, 0}
}
