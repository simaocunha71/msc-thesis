	splitString := strings.Fields(s)
	apples, _ := strconv.Atoi(splitString[0])
	oranges, _ := strconv.Atoi(splitString[2])
	totalFruits := apples + oranges
	return n - totalFruits
}



