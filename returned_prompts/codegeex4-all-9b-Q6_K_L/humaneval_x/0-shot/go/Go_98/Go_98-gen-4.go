```go
func CountUpper(s string) int {
    count := 0
    for i := 0; i < len(s); i += 2 {
        if i%2 == 0 && strings.ContainsRune("AEIOU", rune(s[i])) {
            count++
        }
    }
    return count
}
```

This solution iterates over the string in steps of 2, starting from index 0. For each iteration, it checks if the character at the current index is an uppercase vowel (AEIOU) using the `strings.ContainsRune` function. If the character is an uppercase vowel and the index is even, it increments the count. Finally, it returns the count.