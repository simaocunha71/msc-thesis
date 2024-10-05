Here is a possible solution in Go:
```go
func FindMax(words []string) string {
    maxUnique := 0
    maxWord := ""
    for _, word := range words {
        unique := make(map[rune]bool)
        for _, char := range word {
            unique[char] = true
        }
        if len(unique) > maxUnique {
            maxUnique = len(unique)
            maxWord = word
        }
    }
    return maxWord
}
```
Here's an explanation of the code:

1. We initialize `maxUnique` to 0 and `maxWord` to an empty string. These variables will store the maximum number of unique characters and the corresponding word, respectively.
2. We iterate over each word in the input slice `words`.
3. For each word, we create a map `unique` to store the unique characters. We iterate over each character in the word and add it to the map.
4. We check if the length of the `unique` map is greater than `maxUnique`. If it is, we update `maxUnique` and `maxWord` with the new values.
5. Finally, we return the `maxWord` which has the maximum number of unique characters.

The time complexity of this solution is O(n*m), where n is the number of words and m is the maximum length of a word. The space complexity is O(m), where m is the maximum length of a word.