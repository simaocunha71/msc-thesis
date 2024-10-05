func SeparateParenGroups(paren_string string) []string {
	var result []string
	open := 0
	start := 0
	for i, c := range paren_string {
		if c == '(' {
			open++
			if open == 1 {
				start = i
			}
		} else if c == ')' {
			open--
			if open == 0 {
				result = append(result, paren_string[start:i+1])
			}
		}
	}
	return result
}