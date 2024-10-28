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

This solution iterates from 1 to n and checks if each number is a palindrome. If it is, it checks if it is even or odd and increments the corresponding count. Finally, it returns the counts in a tuple. The time complexity of this solution is O(n^2) due to the palindrome check within the loop.