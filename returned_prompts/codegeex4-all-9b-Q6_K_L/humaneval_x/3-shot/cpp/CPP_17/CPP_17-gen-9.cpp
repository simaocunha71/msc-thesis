To count the distinct characters in a string regardless of case, you can use a map to store the characters as keys. Here's an example of how you can implement the CountDistinctCharacters function in Go:

```go
func CountDistinctCharacters(str string) int {
    distinctChars := make(map[rune]bool)

    for _, char := range str {
        lowerChar := unicode.ToLower(char)
        distinctChars[lowerChar] = true
    }

    return len(distinctChars)
}
```

This implementation iterates over each character in the string and converts it to lowercase using the `unicode.ToLower` function. It then adds the lowercase character to a map as a key, ensuring that each character is only counted once. Finally, it returns the number of keys in the map, which represents the number of distinct characters in the string.

Note that this implementation assumes that the input string consists of Unicode characters. If you need to handle other character sets, you may need to modify the code accordingly.