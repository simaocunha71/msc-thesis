func Digitsum(x string) int {
	sum := 0
	for _, c := range x {
		if unicode.IsUpper(c) {
			sum += int(c)
		}
	}
	return sum
}