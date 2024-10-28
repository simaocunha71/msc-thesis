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

This function checks if a given string is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

Here's the breakdown of the code:

1. `if len(s) < 3 { return false }`: This line checks if the length of the string is less than 3. If it is, the function immediately returns `false` because a string with length less than 3 cannot be happy.

2. `for i := 0; i < len(s)-2; i++ { ... }`: This loop iterates over the string, checking every 3 consecutive letters for distinctness.

3. `if s[i] == s[i+1] || s[i] == s[i+2] || s[i+1] == s[i+2] { return false }`: Inside the loop, this condition checks if any 3 consecutive letters are equal. If they are, the function returns `false` because the string is not happy.

4. `return true`: If the loop finishes without finding any equal 3 consecutive letters, the function returns `true` because the string is happy.

The time complexity of this function is O(n), where n is the length of the string, because it needs to iterate over the string once. The space complexity is O(1), because it only uses a constant amount of space to store the loop index and the string length.