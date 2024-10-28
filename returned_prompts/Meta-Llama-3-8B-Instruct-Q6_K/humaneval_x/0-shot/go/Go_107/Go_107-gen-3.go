```go
func EvenOddPalindrome(n int) [2]int {
    even, odd := 0, 0
    for i := 1; i <= n; i++ {
        s := strconv.Itoa(i)
        if s == reverse(s) {
            if isEven(i) {
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

func isEven(n int) bool {
    return n%2 == 0
}
```
The solution defines three functions: `EvenOddPalindrome`, `reverse`, and `isEven`. 

The `EvenOddPalindrome` function iterates over the range from 1 to `n` and checks each number to see if it's a palindrome. If it is, it checks if it's even or odd and increments the corresponding counter. 

The `reverse` function takes a string as input, reverses its characters, and returns the result as a string. 

The `isEven` function takes an integer as input and returns `true` if it's even, `false` otherwise. 

The function returns a tuple containing the counts of even and odd palindromes in the range from 1 to `n`. 

This solution has a time complexity of O(n), where `n` is the input number, because it iterates over the range from 1 to `n` once. The space complexity is O(1), because it uses a constant amount of space to store the counters and the reversed string. 

This solution works correctly for input numbers up to `10^3`, as required by the problem statement.  However, it may not be efficient for very large input numbers, because it uses a string reversal algorithm that has a time complexity of O(n), where `n` is the length of the input string.  For very large input numbers, a more efficient algorithm that can take advantage of the fact that palindromes are symmetric around their middle character might be needed.  For example, a palindrome with an odd length will have its middle character as its first and last character, and a palindrome with an even length