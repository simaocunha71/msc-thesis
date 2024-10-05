```
func EvenOddPalindrome(n int) [2]int {
    even, odd := 0, 0
    for i := 1; i <= n; i++ {
        s := strconv.Itoa(i)
        if s == reverse(s) {
            if strconv.Itoa(i) == strconv.Itoa(2*i) {
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
In this problem, we need to find the count of even and odd integer palindromes in the range [1, n].
We iterate through the range [1, n] and for each number, we convert it to a string and check if it is a palindrome by comparing it with its reverse. If it is a palindrome, we check if it's even or odd by comparing it with its double. If it's even, we increment the even count, otherwise, we increment the odd count.
Finally, we return the counts as a tuple.

The `reverse` function is used to reverse a string. It works by iterating through the string from both ends and swapping the characters.

Time complexity: O(n)
Space complexity: O(1) (excluding the output tuple)