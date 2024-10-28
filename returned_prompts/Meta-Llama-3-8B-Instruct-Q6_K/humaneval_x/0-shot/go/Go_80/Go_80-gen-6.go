Here is a simple function that checks if a given string is happy or not. It iterates over the string and checks if every 3 consecutive letters are distinct.

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

In this function, we first check if the length of the string is less than 3. If it is, we return false because a string with less than 3 characters cannot be happy. Then we iterate over the string using a for loop. Inside the loop, we check if any 3 consecutive letters are the same by checking if `s[i] == s[i+1] || s[i] == s[i+2] || s[i+1] == s[i+2]`. If we find any 3 consecutive letters that are the same, we return false. If we don't find any, we return true at the end of the function. 

This function has a time complexity of O(n) where n is the length of the string, and a space complexity of O(1) because it uses a constant amount of space. 