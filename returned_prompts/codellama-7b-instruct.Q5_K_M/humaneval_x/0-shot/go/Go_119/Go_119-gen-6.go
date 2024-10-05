	// If the lengths are not equal, it's not possible.
	if len(lst[0]) != len(lst[1]) {
		return "No"
	}

	// If the length is 0, it's possible.
	if len(lst[0]) == 0 {
		return "Yes"
	}

	// The two strings must have the same number of open parentheses.
	var open int
	for i := 0; i < len(lst[0]); i++ {
		if lst[0][i] == '(' {
			open += 1
		} else {
			open -= 1
			if open < 0 {
				break
			}
		}
	}
	for i := 0; i < len(lst[1]); i++ {
		if lst[1][i] == '(' {
			open += 1
		} else {
			open -= 1
			if open < 0 {
				break
			}
		}
	}
	if open != 0 {
		return "No"
	}

	// If there are no open parentheses, it's possible.
	if open == 0 {
		return "Yes"
	}

	// The two strings must have the same number of closed parentheses.
	var closed int
	for i := 0; i < len(lst[0]); i++ {
		if lst[0][i] == ')' {
			closed += 1
		} else {
			closed -= 1
			if closed < 0 {
				break
			}
		}
	}
	for i := 0; i < len(lst[1]); i++ {
		if lst[1][i] == ')' {
			closed += 1
		} else {
			closed -= 1
			if closed < 0 {
				break
			}
		}
	}
	if closed !=