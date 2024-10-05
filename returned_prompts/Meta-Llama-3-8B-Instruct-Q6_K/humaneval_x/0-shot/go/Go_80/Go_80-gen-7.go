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


This Go function checks if a given string `s` is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct. The function iterates over the string with a for loop, checking if any 3 consecutive letters are the same. If it finds any, it immediately returns `false`. If it finishes the loop without finding any, it returns `true`. If the string length is less than 3, it also returns `false` because a happy string must have at least 3 characters. The time complexity is O(n), where n is the length of the string. The space complexity is O(1), as it only uses a constant amount of space.