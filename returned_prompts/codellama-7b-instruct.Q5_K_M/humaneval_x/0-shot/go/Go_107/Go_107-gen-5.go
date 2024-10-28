    var ret [2]int
	var i int
	for i = 1; i <= n; i++ {
		if i == 1 {
			if isPalindrome(i) {
				if isEven(i) {
					ret[0]++
				} else {
					ret[1]++
				}
			}
		} else {
			if isPalindrome(i) {
				if isEven(i) {
					ret[0]++
				} else {
					ret[1]++
				}
			}
		}
	}
	return ret
}

func isPalindrome(n int) bool {
	str := strconv.Itoa(n)
	for i := 0; i < len(str)/2; i++ {
		if str[i] != str[len(str)-i-1] {
			return false
		}
	}
	return true
}

func isEven(n int) bool {
	str := strconv.Itoa(n)
	for i := 0; i < len(str)/2; i++ {
		if str[i] != str[len(str)-i-1] {
			return false
		}
	}
	return true
}

