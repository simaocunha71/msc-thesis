To solve this problem, we need to iterate through each character in the string, convert it to lowercase, and then count how many distinct characters we have seen so far. We can use a map to keep track of the distinct characters.

Here's the Go code:

```go
func CountDistinctCharacters(str string) int {
    distinct := make(map[rune]bool)

    for _, char := range str {
        char = unicode.ToLower(char)
        distinct[char] = true
    }

    return len(distinct)
}
```

This code first creates an empty map called `distinct`. Then, it iterates through each character in the string, converts it to lowercase using the `unicode.ToLower` function, and adds it to the map. Since the map only allows unique keys, the `distinct` map will only contain the distinct characters. Finally, the code returns the length of the `distinct` map, which is the number of distinct characters in the string.