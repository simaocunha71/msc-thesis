```
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


The function `EvenOddPalindrome` takes an integer `n` as input and returns a tuple of two integers, representing the number of even and odd integer palindromes respectively that fall within the range (1, n), inclusive.

The function uses two variables `even` and `odd` to keep track of the count of even and odd integer palindromes respectively.

It then iterates over the range (1, n) using a for loop. For each integer `i` in the range, it checks if the integer is a palindrome by comparing the string representation of `i` with the reverse of the string representation. If `i` is a palindrome, it checks if `i` is even or odd by using the modulo operator `%`. If `i` is even, it increments the `even` count; otherwise, it increments the `odd` count.

Finally, the function returns a tuple of the `even` and `odd` counts using the `[2]int` literal.

This solution has a time complexity of O(n) as it iterates over the range (1, n) once, and a space complexity of O(1) as it uses a constant amount of space to store the `even` and `odd` counts.