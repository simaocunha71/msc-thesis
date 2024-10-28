```go
func EvenOddPalindrome(n int) [2]int {
    var even, odd int
    for i := 1; i <= n; i++ {
        if isPalindrome(i) {
            if i % 2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }
    return [2]int{even, odd}
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
