
// Find how many times a given substring can be found in the original string. Count overlaping cases.
// >>> HowManyTimes('', 'a')
// 0
// >>> HowManyTimes('aaa', 'a')
// 3
// >>> HowManyTimes('aaaa', 'aa')
// 3
func HowManyTimes(str string,substring string) int{
	var count int
	for i:=0;i<len(str);i++{
		if str[i]==substring[0]{
			for j:=0;j<len(substring);j++{
				if str[i+j]==substring[j]{
					if j==len(substring)-1{
						count++
						continue A
					}
				}else{
					break
				}
			}
		}
	}
	return count
}
