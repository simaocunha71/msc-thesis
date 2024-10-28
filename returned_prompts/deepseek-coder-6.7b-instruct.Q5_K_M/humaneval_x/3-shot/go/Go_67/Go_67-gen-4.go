	apples_oranges := strings.Fields(s)
	apples, _ := strconv.Atoi(apples_oranges[0])
	oranges, _ := strconv.Atoi(apples_oranges[2])
	return n - apples - oranges
}



