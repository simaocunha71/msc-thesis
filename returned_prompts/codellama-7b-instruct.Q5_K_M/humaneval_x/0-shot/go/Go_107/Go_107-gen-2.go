	for i := 1; i < n; i++ {
		s := strconv.Itoa(i)
		if len(s) != len(s)/2 {
			continue
		}
		for j := 0; j < len(s)/2; j++ {
			if s[j] != s[len(s)-1-j] {
				continue A
			}
		}
		if i%2 == 0 {
			return [2]int{1, 0}
		}
		return [2]int{0, 1}
	}
	return [2]int{0, 0}
}
