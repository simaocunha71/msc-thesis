```go
func AntiShuffle(s string) string {
    words := strings.Split(s, " ")
    for i, word := range words {
        runes := []rune(word)
        sort.Runes(runes)
        words[i] = string(runes)
    }
    return strings.Join(words, " ")
}
```
Here's an explanation of the code:

1. We split the input string into individual words using the `strings.Split` function.
2. We iterate over each word and convert it to a slice of runes (individual characters) using the `[]rune` type.
3. We use the `sort.Runes` function to sort the runes in ascending order based on their ASCII values.
4. We convert the sorted slice of runes back to a string using the `string` function.
5. We replace the original word with the sorted word in the `words` slice.
6. Finally, we join the sorted words back together into a single string using the `strings.Join` function with a space separator.

You can test this function with the examples you provided:
```