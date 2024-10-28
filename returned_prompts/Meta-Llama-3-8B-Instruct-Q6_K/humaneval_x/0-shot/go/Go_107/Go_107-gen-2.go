```go
func EvenOddPalindrome(n int) [2]int {
    even, odd := 0, 0
    for i := 1; i <= n; i++ {
        s := strconv.Itoa(i)
        if s == reverse(s) {
            if strconv.Itoa(i)[0] == '0' {
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


Explanation:
This problem requires us to count the number of even and odd integer palindromes within the range(1, n), inclusive.

We use two counters, `even` and `odd`, to store the count of even and odd integer palindromes respectively.

For each number `i` from 1 to `n`, we convert it to a string `s` and check if it is a palindrome by comparing it with its reverse. If it is a palindrome, we then check if the first digit is 0 (in which case it is even) or not (in which case it is odd).

Finally, we return the tuple `[even, odd]`.

The `reverse` function is used to reverse the string representation of a number.

This solution has a time complexity of O(n) where n is the input number, and a space complexity of O(1) since we are using a constant amount of space.