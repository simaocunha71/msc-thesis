Here is the Go code that solves the problem:

```go
import (
    "bytes"
    "strings"
)

func GetClosestVowel(word string) string {
    bytesWord := []byte(word)
    vowels := []byte("aeiouAEIOU")

    for i := len(bytesWord) - 1; i >= 0; i-- {
        if bytes.IndexByte(vowels, bytesWord[i]) != -1 {
            for j := i - 1; j >= 0; j-- {
                if bytes.IndexByte(vowels, bytesWord[j]) == -1 {
                    return string(bytesWord[j+1 : i+1])
                }
            }
            return string(bytesWord[:i+1])
        }
    }
    return ""
}
```

This code iterates over the word from right to left. If it finds a vowel, it checks the characters to its left. If it finds a consonant (i.e., a character that is not a vowel), it returns the substring from the consonant to the vowel. If it doesn't find a consonant, it returns the substring from the vowel to the end of the word. If it doesn't find any vowel, it returns an empty string. The function is case sensitive, so it treats uppercase and lowercase vowels as different characters. The function also returns the first vowel that meets the condition, so if there are multiple vowels that meet the condition, it will return the one that is closest to the beginning of the word.