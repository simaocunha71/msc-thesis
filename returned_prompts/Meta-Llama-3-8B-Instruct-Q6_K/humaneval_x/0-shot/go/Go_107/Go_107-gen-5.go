```go
func EvenOddPalindrome(n int) [2]int {
    even := 0
    odd := 0
    for i := 1; i <= n; i++ {
        str := strconv.Itoa(i)
        if len(str) > 1 && str == strconv.Itoa(i)[::-1] {
            if strconv.Atoi(str) % 2 == 0 {
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
The problem is asking to find the number of even and odd integer palindromes within the range (1, n), inclusive. We can solve this problem by iterating through each number from 1 to n, converting it to a string, checking if it's a palindrome, and then checking if it's even or odd.

In the code above, we initialize two variables `even` and `odd` to 0 to keep track of the number of even and odd palindromes respectively. We then iterate through each number from 1 to n. For each number, we convert it to a string using `strconv.Itoa(i)`, check if its length is greater than 1 (since single-digit numbers are not palindromes), and then check if the string is equal to its reverse using slicing (`str == strconv.Itoa(i)[::-1]`).

If the number is a palindrome, we check if it's even or odd by converting the string back to an integer using `strconv.Atoi(str)` and checking if it's divisible by 2. If it's even, we increment `even`, otherwise we increment `odd`.

Finally, we return a tuple containing the values of `even` and `odd` using `[2]int{even, odd}`.