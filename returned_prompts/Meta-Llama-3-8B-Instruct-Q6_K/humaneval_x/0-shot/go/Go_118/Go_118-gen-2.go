Here is the solution:
```go
func GetClosestVowel(word string) string {
    vowels := []byte("aeiouAEIOU")
    for i := len(word) - 1; i > 0; i-- {
        if bytes.IndexByte(vowels, word[i]) != -1 {
            return string(word[i : i+1])
        }
    }
    return ""
}
```
Explanation:

We iterate through the word from right to left (i.e., from the end of the word to the beginning). We check if the current character is a vowel by using the `bytes.IndexByte` function, which returns the index of the first occurrence of the specified byte in the byte slice. If it is a vowel, we return the vowel as a string.

If we reach the beginning of the word without finding a vowel, we return an empty string. This is because the problem statement specifies that we should not consider vowels at the beginning or end of the word.