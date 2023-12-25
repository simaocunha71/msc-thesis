
// Find how many times a given substring can be found in the original string. Count overlaping cases.
// >>> HowManyTimes('', 'a')
// 0
// >>> HowManyTimes('aaa', 'a')
// 3
// >>> HowManyTimes('aaaa', 'aa')
// 3
func HowManyTimes(str string,substring string) int{
	if len(substring) == 0 { return 1}
    
    // Create a map of characters to their occurrence count as the string is parsed. 
    // The substring's occurrence is tracked in the substringMap.
    strMap := make(map[rune]int)
    substringMap := make(map[char]int)
    
    for i, c := range str {
        if c == ',' && len(substringMap) > 0 {
            strMap := make(map[rune]int)
            for j, k := range substringMap {
                strMap[k] += 1
                substringMap[j] = strMap
            }
        } else {
            strMap[c]++
        }
    }
    
    // Count the number of occurrences of substring in str. It is handled by a helper function that counts overlapping cases.
    strCount, _ := CountSubstring(strMap, substring)
    return int(strCount.(float64))
}
func CountSubstring(substringMap map[char]int,substring string){
    
	var lastFoundPosition = 0
    	var currentFoundPosition index
    	var count = 1
    	for _,ch := range substring{
        	if substringMap[ch] > 0{
            	substringMap[ch]-=1
            if substringMap[ch] == 0 && count==1 {
                return currentFoundPosition,ch
            } else {
                    count+=1
                }}else{
    		if substring[currentFoundPosition] != ch {
        	lastFoundPosition = FindNextIndex(substringMap, lastFoundPosition + 1)
            	substringMap[ch]++
                currentFoundPosition = lastFoundPosition
        }}}
    return currentFoundPosition,ch
}
func FindNextIndex(