Here is a Go function that solves the problem:

```go
func GetClosestVowel(word string) string {
    vowels := "aeiouAEIOU"
    for i := len(word) - 1; i >= 0; i-- {
        if string(word[i]) == string(vowels[0]) {
            return string(word[i])
        }
    }
    return ""
}
```

This function iterates over the word from right to left. It checks each character to see if it is a vowel. If it finds a vowel, it returns that vowel. If it doesn't find any vowel, it returns an empty string. 

This function is case sensitive, so it will treat 'a' and 'A' as different characters. If you want to make it case insensitive, you can convert the word to lowercase or uppercase before processing it. 

This function has a time complexity of O(n), where n is the length of the word. This is because it needs to iterate over the word once to find the closest vowel. The space complexity is O(1), which means it uses a constant amount of space, regardless of the size of the input. This is because it only uses a fixed amount of space to store the vowels and the word. 

Please note that this function assumes that the input word contains only English letters. If the word can contain other characters, you may need to add error checking code to handle those cases. 