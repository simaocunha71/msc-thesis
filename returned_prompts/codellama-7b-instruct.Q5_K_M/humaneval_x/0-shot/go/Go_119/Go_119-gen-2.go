	for i := range lst {
		for j := range lst {
			if i == j {
				continue
			}
			if (lst[i] == "(" && lst[j] == ")") || (lst[i] == ")" && lst[j] == "(") {
				continue A
			}
		}
		return "No"
	}
	return "Yes"
}
