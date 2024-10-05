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


Explanation:
The given problem is to check if a given string is happy or not. A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct.

Here is a simple solution in Go:

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

In this solution, we first check if the length of the string is less than 3. If it is, we immediately return false as per the problem's definition.

Then, we iterate over the string from the start to the end (excluding the end as we only need to check 3 consecutive characters at a time). For each character, we check if it is equal to the next two characters. If it is, we return false as per the problem's definition.

If we finish the iteration without returning false, we return true as the string is considered happy.

This solution has a time complexity of O(n), where n is the length of the string, and a space complexity of O(1) as we are not using any extra space that scales with the input size.