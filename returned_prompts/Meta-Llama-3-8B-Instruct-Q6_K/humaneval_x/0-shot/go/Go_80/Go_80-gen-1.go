Here is a Go solution for the problem:

```go
func IsHappy(s string) bool {
    if len(s) < 3 {
        return false
    }
    for i := 0; i < len(s)-2; i++ {
        if s[i] == s[i+1] || s[i] == s[i+2] {
            return false
        }
    }
    return true
}
```

This function first checks if the length of the string is less than 3. If it is, it returns false because a happy string must have at least 3 characters. Then it iterates over the string, checking if any three consecutive characters are the same. If it finds any, it returns false. If it doesn't find any, it returns true, indicating that the string is happy.