
// Find how many times a given substring can be found in the original string. Count overlaping cases.
// >>> HowManyTimes('', 'a')
// 0
// >>> HowManyTimes('aaa', 'a')
// 3
// >>> HowManyTimes('aaaa', 'aa')
// 3
func HowManyTimes(str string,substring string) int{
	if substring == "" {
		return len(str)
	}else if substring == str {
		return 1;
	}
	var lastIndex int = -1
	for i := 0;i<len(str);i++ {
		if str[i] == substring{
			lastIndex = i+1;
		}else{
			if lastIndex != -1 && (substring == str[lastIndex-1] || substring == str[lastIndex]){
				lastIndex++
			} else {
				lastIndex = -1;
			}
		}
	}
	return lastIndex + 1;
}