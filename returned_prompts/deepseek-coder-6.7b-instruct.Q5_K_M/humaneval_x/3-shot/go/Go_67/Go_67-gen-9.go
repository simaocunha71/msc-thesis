	splitString := strings.Split(s," ")
	apples, _ := strconv.Atoi(splitString[2])
	oranges, _ := strconv.Atoi(splitString[6])
	return n - apples - oranges

}



