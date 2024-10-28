```go
func EvenOddPalindrome(n int) [2]int {
    even, odd := 0, 0
    for i := 1; i <= n; i++ {
        s := strconv.Itoa(i)
        if s == reverse(s) {
            if strconv.Itoa(i) % 2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }
    return [2]int{even, odd}
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```


The above solution is based on the idea of iterating through all numbers from 1 to n, and for each number, check if it is a palindrome. If it is, then check if it is even or odd. If it is even, increment the even counter, otherwise increment the odd counter. Finally, return the counts as a tuple.

The `reverse` function is used to reverse a string, which is used to check if a number is a palindrome. The `strconv.Itoa` function is used to convert an integer to a string, and the `%` operator is used to check if a number is even or odd.

The time complexity of this solution is O(n), where n is the input number. The space complexity is O(1), as it only uses a constant amount of space to store the counters and the reversed string.