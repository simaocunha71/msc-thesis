
	for i := 0; i < len(lst); i++ {
		for j := i + 1; j < len(lst); j++ {
			if (lst[i] == "(" && lst[j] == ")") || (lst[i] == ")" && lst[j] == ")") {
				continue A
			}
		}
	}
	return "Yes"

}
