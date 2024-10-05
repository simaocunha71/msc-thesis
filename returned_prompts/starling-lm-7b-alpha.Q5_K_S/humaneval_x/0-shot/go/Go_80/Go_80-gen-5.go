To solve this problem, I would follow these steps:

1. Initialize a map to store previously encountered substrings.
2. Initialize a boolean variable to track whether the current substring is happy or not.
3. Iterate through the string in chunks of length 3, starting from index 2 (since the first two characters don't have any preceding characters).
4. For each chunk of three characters, check if it is already present in the map. If it is, set the boolean variable to false and break out of the loop.
5. If the boolean variable is still true after iterating through all chunks, return true. Otherwise, return false.

Here's an example implementation of the above approach:

```go
func IsHappy(s string) bool {
    m := make(map[string]bool)
    happy := true
    for i := 2; i < len(s); i++ {
        sub := s[i-2 : i+1]
        if m[sub] {
            happy = false
            break
        }
        m[sub] = true
    }
    return happy
}
```

In this implementation, the `m` map is used to store previously encountered substrings. The `happy` boolean variable is initially set to true. The `for` loop iterates through the string in chunks of length 3, starting from index 2. For each chunk, it checks if it is already present in the map. If it is, the `happy` variable is set to false and the loop is broken. If all chunks pass the check, the `happy` variable remains true and the function returns true. Otherwise, it returns false.

This approach has a time complexity of O(n) and a space complexity of O(n/3), where n is the length of the input string.

```go
func IsHappy(s string) bool {
    m := make(map[string]bool)
    happy := true
    for i := 2; i < len(s); i++ {
        sub := s[i-2 : i+1]
        if m[sub] {
            happy = false
            break
        }
        m[sub] = true
    }
    return happy
}
```