```go
func CountDistinctCharacters(str string) int {
    distinctCharacters := map[rune]bool{}
    for _, char := range strings.ToLower(str) {
        distinctCharacters[char] = true
    }
    return len(distinctCharacters)
}
```

Explanation:
1. We create a map `distinctCharacters` to store the distinct characters.
2. We convert the string to lowercase using `strings.ToLower(str)` to ignore case sensitivity.
3. We iterate over each character `char` in the string.
4. We add each character to the map `distinctCharacters` with its value set to true.
5. We return the length of the map `distinctCharacters` which represents the number of distinct characters in the string.