```go
func IsHappy(s string) bool {
    if len(s) < 3 {
        return false
    }
    for i := 0; i < len(s)-2; i++ {
        if s[i] == s[i+1] || s[i] == s[i+2] || s[i+1] == s[i+2] {
            return false
        }
    }
    return true
}
```


The function `IsHappy(s string) bool` checks if the given string `s` is happy or not. A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct.

Here's how it works:

1. If the length of the string is less than 3, it immediately returns `false` as the string cannot be happy with a length less than 3.
2. It then iterates through the string, checking every 3 consecutive letters. If it finds any 3 consecutive letters that are the same, it returns `false` as the string is not happy.
3. If it checks all 3 consecutive letters and doesn't find any duplicates, it returns `true`, indicating that the string is happy.

For example, if the input is "abcd", it checks the first 3 letters ("abc") and finds them distinct. It then moves on to the next 3 letters ("bcd") and finds them distinct as well. Since it doesn't find any duplicates, it returns `true`, indicating that the string is happy.

If the input is "aabb", it checks the first 3 letters ("aaa") and finds them not distinct. It returns `false` immediately, indicating that the string is not happy.