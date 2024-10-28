Here is the solution in Go:

```go
func GetClosestVowel(word string) string {
    var closestVowel string
    for i := len(word) - 1; i >= 0; i-- {
        if "aeiouAEIOU"[0] <= byte(word[i]) && byte(word[i]) <= "aeiouAEIOU"[9] {
            closestVowel = string(word[i])
            break
        }
    }
    if closestVowel == "" {
        for i := 0; i < len(word); i++ {
            if "aeiouAEIOU"[0] <= byte(word[i]) && byte(word[i]) <= "aeiouAEIOU"[9] {
                closestVowel = string(word[i])
                break
            }
        }
    }
    return closestVowel
}
```

This solution iterates through the word from the right to the left to find the closest vowel. If no vowel is found, it then iterates through the word from left to right. The closest vowel is the one that is closest to the center of the word. If no vowel is found, the function returns an empty string. 

Note: This solution assumes that the input word is a non-empty string. If the input word can be an empty string, you should add a check for this at the beginning of the function. 

Also, this solution is case sensitive, meaning it treats uppercase and lowercase vowels as different characters. If you want to make it case insensitive, you can convert the word to either lowercase or uppercase before searching for the closest vowel. 

The time complexity of this solution is O(n), where n is the length of the input word. The space complexity is O(1), as it only uses a constant amount of space to store the closest vowel. 