Here is a solution in Go:

```go
func SelectWords(s string, n int) []string {
    words := strings.Fields(s)
    result := make([]string, 0, len(words))
    for _, word := range words {
        consonants := 0
        for _, c := range word {
            if c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'y' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U' && c != 'Y' {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}
```

The function `SelectWords` takes a string `s` and a natural number `n` as input. It first splits the string into words using `strings.Fields`, then it iterates over each word. For each word, it counts the number of consonants by checking if each character is not a vowel. If the number of consonants is equal to `n`, the word is added to the result list. Finally, the function returns the result list.

Note: The function does not consider 'y' as a vowel. If you want to consider 'y' as a vowel, you should remove the condition `c != 'y' && c != 'Y'` from the loop.