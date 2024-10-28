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

func isPalindrome(num int) bool {
    str := strconv.Itoa(num)
    for i := 0; i < len(str)/2; i++ {
        if str[i] != str[len(str)-1-i] {
            return false
        }
    }
    return true
}
```

