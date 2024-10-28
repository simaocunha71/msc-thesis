```go
func EvenOddPalindrome(n int) [2]int {
	evenCount, oddCount := 0, 0
	for i := 1; i <= n; i++ {
		if isPalindrome(i) {
			if i % 2 == 0 {
				evenCount++
			} else {
				oddCount++
			}
		}
	}
	return [2]int{evenCount, oddCount}
}

func isPalindrome(x int) bool {
	s := strconv.Itoa(x)
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}
```
