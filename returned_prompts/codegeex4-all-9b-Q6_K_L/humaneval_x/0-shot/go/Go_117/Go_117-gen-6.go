To implement the `SelectWords` function, you can follow these steps:

1. Split the input string `s` into words using `strings.Fields`.
2. Iterate over each word in the resulting slice.
3. For each word, count the number of consonants by iterating over its characters and checking if each character is a consonant.
4. If a word contains exactly `n` consonants, add it to a result slice.
5. Return the result slice.

Here's the complete implementation:

```go
func SelectWords(s string, n int) []string {
    words := strings.Fields(s)
    result := []string{}
    for _, word := range words {
        if countConsonants(word) == n {
            result = append(result, word)
        }
    }
    return result
}

func countConsonants(s string) int {
    consonants := "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count := 0
    for _, char := range s {
        if strings.ContainsRune(consonants, char) {
            count++
        }
    }
    return count
}
```

You can test the function with the provided examples:

```go
func main() {
    fmt.Println(SelectWords("Mary had a little lamb", 4)) // ==> ["little"]
    fmt.Println(SelectWords("Mary had a little lamb", 3)) // ==> ["Mary", "lamb"]
    fmt.Println(SelectWords("simple white space", 2)) // ==> []
    fmt.Println(SelectWords("Hello world", 4)) // ==> ["world"]
    fmt.Println(SelectWords("Uncle sam", 3)) // ==> ["Uncle"]
}
```

This will output the expected results.