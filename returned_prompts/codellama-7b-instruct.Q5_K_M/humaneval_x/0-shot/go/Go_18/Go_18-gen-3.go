
// Find how many times a given substring can be found in the original string. Count overlaping cases.
// >>> HowManyTimes('', 'a')
// 0
// >>> HowManyTimes('aaa', 'a')
// 3
// >>> HowManyTimes('aaaa', 'aa')
// 3
func HowManyTimes(str string,substring string) int{

	var counter int
	for i:=0; i < len(str); i++ {
		for j:=0; j < len(substring); j++ {
			if len(str) < i+j {
				break
			}
			if str[i+j] != substring[j] {
				break
			}
			if j == len(substring) - 1 {
				counter++
			}
		}
	}
	return counter
}
