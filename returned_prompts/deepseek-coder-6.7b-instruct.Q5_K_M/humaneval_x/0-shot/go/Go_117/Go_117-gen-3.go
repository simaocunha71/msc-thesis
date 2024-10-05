    var words []string
    var result []string
    var buffer bytes.Buffer
    vowels := "aeiouAEIOU"

    for _, char := range s {
        if char != ' ' {
            buffer.WriteRune(char)
        } else {
            words = append(words, buffer.String())
            buffer.Reset()
        }
    }
    words = append(words, buffer.String())

    for _, word := range words {
        count := 0
        for _, letter := range word {
            if !strings.ContainsRune(vowels, letter) {
                count++
            }
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}
```

**Explanation:**
In this program, we first split the given string `s` into a slice of words. We use a byte buffer to build each word, and whenever we see a space, we know we've reached the end of a word, so we add it to our slice of words and reset the buffer.

Then, we iterate over each word in our slice of words, and for each word, we count the number of consonants. If the count matches the given number `n`, we add the word to our result slice.

Finally, we return the result slice.

**Complexity Analysis:**
Time Complexity: O(n), where n is the length of the string s. We do two passes over the string: one to split it into words, and one to count the number of consonants in each word.

Space Complexity: O(n), where n is the number of words in the string s. We store the words in a slice and the result in a separate slice.

**Test Cases:**
```go
func main() {
    fmt.Println(SelectWords("Mary had a little lamb", 4))  // ["little"]
    fmt.Println(SelectWords("Mary had a little lamb", 3))  // ["Mary", "lamb"]
    fmt.Println(SelectWords("simple white space", 2))     // []
    fmt.Println