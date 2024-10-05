func HowManyTimes(str string, substring string) int {
	if len(str) == 0 || len(substring) == 0 {
		return 0
	}
	count := 0
	for i := 0; i <= len(str)-len(substring); i++ {
		if str[i:i+len(substring)] == substring {
			count++
		}
	}
	return count
}