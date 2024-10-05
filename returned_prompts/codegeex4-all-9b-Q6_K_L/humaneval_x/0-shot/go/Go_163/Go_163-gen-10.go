func GenerateIntegers(a, b int) []int {
	var result []int

	for i := a; i <= b; i++ {
		for _, v := range strconv.Itoa(i) {
			if v%2 == 0 {
				result = append(result, v)
			}
		}
	}

	return result
}