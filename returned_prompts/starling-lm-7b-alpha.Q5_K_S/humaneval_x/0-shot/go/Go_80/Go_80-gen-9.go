To solve this problem, we need to iterate through the string and check every 3 consecutive letters to see if they are distinct. We can do this by using a sliding window technique.

Here's a step-by-step explanation of the solution:

1. Create a sliding window that moves through the string, selecting 3 consecutive letters at a time.
2. Create a map called "m" to store the 3 consecutive letters as keys and their indexes as values. This will allow us to quickly check if the letters are distinct.
3. Check if the length of the string is less than 3. If it is, return false, as we need at least 3 consecutive letters to determine if the string is happy or not.
4. Iterate through the string using the sliding window technique, updating the map "m" and checking if the 3 consecutive letters are distinct. If they are not, return false.
5. If we have iterated through the entire string without finding any non-distinct 3 consecutive letters, return true.

Here's an example implementation in Go:

```go
func IsHappy(s string) bool {
    if len(s) < 3 {
        return false
    }
    m := make(map[string]int)
    for i := 0; i < len(s)-2; i++ {
        key := s[i:i+3]
        if m[key] != 0 {
            return false
        }
        m[key] = i + 3
    }
    return true
}
```

In this example, the function `IsHappy` takes a string `s` as input and returns a boolean value indicating whether the string is happy or not. It first checks if the length of the string is less than 3, and if so, it immediately returns false. Then, it creates a map called `m` to store the 3 consecutive letters as keys and their indexes as values. It then iterates through the string using a sliding window technique, updating the map `m` and checking if the 3 consecutive letters are distinct. If they are not, it returns false. If it has iterated through the entire string without finding any non-distinct 3 consecutive letters, it returns true.

The time complexity of this solution is O