	apples, oranges := strings.Split(s, "and")[0], strings.Split(s, "and")[1]
	apples_n, _ := strconv.Atoi(strings.TrimSpace(apples))
	oranges_n, _ := strconv.Atoi(strings.TrimSpace(oranges))
	return n - apples_n - oranges_n
}



