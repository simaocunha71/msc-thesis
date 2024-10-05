	split := strings.Split(s, " ")
	apples, _ := strconv.Atoi(split[2])
	oranges, _ := strconv.Atoi(split[6])
	return n - apples - oranges
}


