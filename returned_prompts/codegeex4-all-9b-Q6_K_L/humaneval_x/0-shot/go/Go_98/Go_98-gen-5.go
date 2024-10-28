```go
func CountUpper(s string) int {
    var count int = 0
    for i := 0; i < len(s); i += 2 {
        if strings.ContainsRune("AEIOU", rune(s[i])) {
            count++
        }
    }
    return count
}
```

In this function, we iterate over the string `s` with a step of 2, starting from index 0. For each character at an even index, we check if it is an uppercase vowel by using the `strings.ContainsRune` function. If it is, we increment the `count` variable. Finally, we return the `count` variable, which represents the number of uppercase vowels in even indices.