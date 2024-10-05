```
func VowelsCount(s string) int {
    var count int
    for _, char := range s {
        switch {
        case strings.ToLower(string(char)) == "a":
            count++
        case strings.ToLower(string(char)) == "e":
            count++
        case strings.ToLower(string(char)) == "i":
            count++
        case strings.ToLower(string(char)) == "o":
            count++
        case strings.ToLower(string(char)) == "u":
            count++
        case strings.HasSuffix(s, string(char)) && strings.ToLower(string(char)) == "y":
            count++
        }
    }
    return count
}
```


The function `VowelsCount` counts the number of vowels in a given string. It iterates over each character in the string. For each character, it checks if it is a vowel. If the character is 'y' and it is at the end of the string, it also counts as a vowel. The function returns the total count of vowels. The function uses the `strings` package to convert the character to lowercase and to check if a string ends with a certain suffix.

The time complexity of this function is O(n), where n is the length of the input string, because it needs to iterate over each character in the string. The space complexity is O(1), because it only uses a constant amount of space to store the count of vowels.