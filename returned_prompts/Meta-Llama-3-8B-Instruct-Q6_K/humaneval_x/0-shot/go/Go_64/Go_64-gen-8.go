```go
func VowelsCount(s string) int {
    s = strings.ToLower(s)
    count := 0
    for _, char := range s {
        if char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u' {
            if char == 'y' && s[len(s)-1] == 'y' {
                continue
            }
            count++
        }
    }
    return count
}
```

Explanation:

1. We convert the input string `s` to lowercase using `strings.ToLower(s)` to ensure that the count is case-insensitive.
2. We initialize a `count` variable to keep track of the number of vowels.
3. We iterate through each character `char` in the string using a range-based loop.
4. For each character, we check if it's a vowel (i.e., 'a', 'e', 'i', 'o', or 'u') using an if statement.
5. If the character is 'y', we check if it's at the end of the string using `s[len(s)-1] == 'y'`. If it is, we skip it using `continue` to avoid counting it as a vowel.
6. If the character is a vowel, we increment the `count` variable.
7. Finally, we return the `count` variable, which represents the number of vowels in the input string.