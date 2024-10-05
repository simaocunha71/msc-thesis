	splits := strings.Fields(s)
	apples, _ := strconv.Atoi(splits[0])
	oranges, _ := strconv.Atoi(splits[2])
	return n - apples - oranges
}



