	// write your solution here, use this for reference: https://www.youtube.com/watch?v=L5tKhF5UJYM
	str := strings.Split(s, " ")
	apples, err := strconv.Atoi(str[0])
	oranges, err := strconv.Atoi(str[1])
	mango := n - apples - oranges
	return mango
}