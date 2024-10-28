func FizzBuzz(n int) int {
	var count int
	for i := 1; i < n; i++ {
		if i%11 == 0 || i%13 == 0 {
			str := strconv.Itoa(i)
			for j := 0; j < len(str); j++ {
				if str[j] == '7' {
					count++
				}
			}
		}
	}
	return count
}
