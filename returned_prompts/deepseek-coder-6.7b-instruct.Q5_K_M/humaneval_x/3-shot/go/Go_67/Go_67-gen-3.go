	splitString := strings.Split(s, " ")
	appleCount, _ := strconv.Atoi(splitString[2])
	orangeCount, _ := strconv.Atoi(splitString[6])

	return n - appleCount - orangeCount
}



