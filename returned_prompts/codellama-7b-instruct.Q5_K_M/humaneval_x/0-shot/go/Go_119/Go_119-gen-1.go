
	for i := 0; i < len(lst); i++ {
		for j := 0; j < len(lst[i]); j++ {
			if !(lst[i][j] == '(' || lst[i][j] == ')') {
				return "No"
			}
		}
	}
	for i := 0; i < len(lst); i++ {
		for j := 0; j < len(lst[i]); j++ {
			if lst[i][j] == '(' {
				if lst[i][j+1] == ')' {
					return "Yes"
				}
			}
		}
	}
	return "No"
}
