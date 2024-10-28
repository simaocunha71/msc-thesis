	words := strings.Fields(s)
	apples, _ := strconv.Atoi(words[0])
	oranges, _ := strconv.Atoi(words[3])
	
	return n - apples - oranges
}



