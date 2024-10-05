Here is the solution:

```go
func RemoveVowels(text string) string {
    var result string
    for _, char := range text {
        if char != 'a' && char != 'e' && char != 'i' && char != 'o' && char != 'u' && char != 'A' && char != 'E' && char != 'I' && char != 'O' && char != 'U' {
            result += string(char)
        }
    }
    return result
}
```



Explanation:
The function `RemoveVowels` takes a string `text` as input and returns a new string without vowels. It iterates over each character in the input string using a range-based for loop. For each character, it checks if the character is not a vowel (both lowercase and uppercase) using a conditional statement. If the character is not a vowel, it adds the character to the result string using the `result += string(char)` statement. Finally, it returns the result string.