Here's how you can define the function in Go:

```go
func CountDistinctCharacters(str string) int {
    str = strings.ToLower(str)
    charMap := make(map[rune]bool)
    for _, char := range str {
        charMap[char] = true
    }
    return len(charMap)
}
```

In this function, we first convert the string to lowercase to ignore the case of the characters. Then, we create a map to store the distinct characters. We iterate over each character in the string and add it to the map. The second value of the pair in the map is always `true`, so we don't need to store it. Finally, we return the length of the map, which is the number of distinct characters in the string.

This function has a time complexity of O(n), where n is the length of the string.