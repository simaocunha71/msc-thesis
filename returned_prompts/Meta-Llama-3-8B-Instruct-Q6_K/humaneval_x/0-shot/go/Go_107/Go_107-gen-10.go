```go
func EvenOddPalindrome(n int) [2]int {
    even := 0
    odd := 0
    for i := 1; i <= n; i++ {
        s := strconv.Itoa(i)
        if s == reverse(s) {
            if i%2 == 0 {
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
The code defines a function `EvenOddPalindrome` that takes an integer `n` as input and returns a tuple containing the number of even and odd integer palindromes within the range `[1, n]`.

The function iterates over the range `[1, n]` and checks each integer `i` to see if it is a palindrome by converting it to a string and comparing it with its reverse. If `i` is a palindrome, it checks if `i` is even or odd and increments the corresponding counter.

The `reverse` function is a helper function that reverses a given string.

The time complexity of the code is O(n), where `n` is the input integer, because it needs to iterate over the range `[1, n]`. The space complexity is O(1), because it only uses a constant amount of space to store the counters and the reversed string.