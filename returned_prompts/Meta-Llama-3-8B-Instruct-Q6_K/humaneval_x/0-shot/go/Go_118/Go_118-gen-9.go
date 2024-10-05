Here is a Go solution using a simple loop to iterate over the characters in the word:

```go
func GetClosestVowel(word string) string {
    vowels := []byte("aeiouAEIOU")
    for i := len(word) - 1; i >= 0; i-- {
        if bytes.IndexByte(vowels, word[i]) != -1 {
            for j := i - 1; j >= 0; j-- {
                if !isConsonant(word[j]) {
                    return string(word[i])
                }
            }
            return string(word[i])
        }
    }
    return ""
}

func isConsonant(b byte) bool {
    vowels := []byte("aeiouAEIOU")
    for _, v := range vowels {
        if v == b {
            return false
        }
    }
    return true
}
```

In the `GetClosestVowel` function, we iterate over the word from right to left. If we find a vowel, we then iterate from left to right until we find a non-vowel (consonant). The first vowel we find that is not preceded by a vowel is the closest vowel to the right of two consonants. If no such vowel is found, we return an empty string.

The `isConsonant` function is a helper function that checks if a character is a vowel or not. It does this by iterating over the vowels and checking if the character is equal to any of them. If it is, it returns `false` (the character is a vowel), otherwise it returns `true` (the character is a consonant).