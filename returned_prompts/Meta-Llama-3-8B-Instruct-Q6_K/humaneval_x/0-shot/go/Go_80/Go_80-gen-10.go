```go
func IsHappy(s string) bool {
    n := len(s)
    if n < 3 {
        return false
    }
    for i := 0; i < n-2; i++ {
        set := make(map[string]bool)
        for j := i; j < i+3; j++ {
            set[s[j]] = true
        }
        if len(set) != 3 {
            return false
        }
    }
    return true
}
```


The function `IsHappy(s string)` checks if the given string `s` is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct. The function returns `true` if the string is happy and `false` otherwise.

The function first checks if the length of the string is less than 3. If it is, the function immediately returns `false` because a string with a length less than 3 cannot be happy.

Then, the function iterates over the string in steps of 3. For each step, it creates a map `set` to store the distinct characters in the current 3-character slice of the string. If the length of the `set` is not 3, it means that the current 3-character slice is not distinct, so the function returns `false`.

If the function finishes iterating over the string without returning `false`, it means that every 3-character slice of the string is distinct, so the function returns `true`. This means that the string is happy.