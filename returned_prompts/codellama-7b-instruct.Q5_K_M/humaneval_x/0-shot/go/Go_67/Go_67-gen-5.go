	// first we get the number of the apples and the number of the oranges
	// we get the number of the apples
	apples, _ := strconv.Atoi(strings.Split(s, " ")[0])
	// we get the number of the oranges
	oranges, _ := strconv.Atoi(strings.Split(s, " ")[1])
	// we return the number of the mango fruits in the basket
	return n - apples - oranges
}

