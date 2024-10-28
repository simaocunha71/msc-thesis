```go
func EvenOddPalindrome(n int) [2]int {
    even, odd := 0, 0
    for i := 1; i <= n; i++ {
        if strconv.Itoa(i) == strconv.Itoa(i)[::-1] {
            if i%2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }
    return [2]int{even, odd}
}
```


Explanation:
1. Initialize two counters, `even` and `odd`, to keep track of the number of even and odd integer palindromes respectively.
2. Iterate from 1 to `n` (inclusive).
3. For each integer `i`, convert it to a string using `strconv.Itoa(i)` and check if it's a palindrome by comparing it with its reverse using slicing (`strconv.Itoa(i)[::-1]`).
4. If `i` is a palindrome, check if it's even by using the modulo operator (`i % 2 == 0`). If it's even, increment `even`, otherwise increment `odd`.
5. Return a tuple containing the counts of even and odd integer palindromes as `[2]int{even, odd}`.