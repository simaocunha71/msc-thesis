	var ans []int

	for _, group := range strings.Split(paren_string, " ") {
		var max_depth int
		for _, r := range group {
			if r == '(' {
				max_depth++
			} else if r == ')' {
				max_depth--
			}
		}
		ans = append(ans, max_depth)
	}
	return ans
}
