// Write your code here
	var interval [2]int
	if interval1[0] > interval2[0] {
		interval[0] = interval1[0]
	} else {
		interval[0] = interval2[0]
	}

	if interval1[1] < interval2[1] {
		interval[1] = interval1[1]
	} else {
		interval[1] = interval2[1]
	}

	if interval[0] > interval[1] {
		return "NO"
	}

	// 判断是否为素数
	if isPrime(interval[1]-interval[0]+1) {
		return "YES"
	} else {
		return "NO"
	}

}

//判断素数
func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// 使用golang 实现的素数判断
func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}