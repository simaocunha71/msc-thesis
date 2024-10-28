Here is a simple function in Go that implements the described functionality:

```go
import (
    "bytes"
    "strings"
)

func GetClosestVowel(word string) string {
    vowels := "aeiouAEIOU"
    for i := len(word) - 1; i >= 0; i-- {
        if strings.IndexRune(vowels, word[i]) != -1 {
            for j := i - 1; j >= 0; j-- {
                if !strings.ContainsRune(vowels, word[j]) {
                    return string(word[i])
                }
            }
        }
    }
    return ""
}
```

This function iterates over the word from right to left. It checks each character if it's a vowel. If it is, it then iterates over the characters to the left until it finds a consonant. The first vowel it finds in this process is returned. If no vowel is found, an empty string is returned. 

Note that the function is case sensitive, so it treats uppercase and lowercase vowels as different characters. If you want it to be case insensitive, you can convert the word to either lowercase or uppercase before processing it. 

This function has a time complexity of O(n), where n is the length of the word, because in the worst-case scenario it needs to iterate over the entire word. The space complexity is O(1), because it uses a constant amount of space. 