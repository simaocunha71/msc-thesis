```go
func VowelsCount(s string) int {
    s = strings.ToLower(s) // convert to lowercase
    count := 0
    for _, v := range s {
        if v == 'a' || v == 'e' || v == 'i' || v == 'o' || v == 'u' {
            count++
        }
    }
    if s[len(s)-1] == 'y' { // check if 'y' is at the end
        count++
    }
    return count
}
```
Explanation:
1. We use the `strings.ToLower(s)` function to convert the input string to lowercase. This is to ensure that the function works correctly for words that contain uppercase letters.
2. We initialize a variable `count` to 0, which will be used to store the number of vowels in the string.
3. We iterate over each character `v` in the string using a range loop.
4. For each character, we check if it is a vowel by comparing it to 'a', 'e', 'i', 'o', or 'u'. If it is a vowel, we increment the `count` variable.
5. After iterating over all characters, we check if the last character of the string is 'y'. If it is, we increment the `count` variable again, since 'y' is a vowel at the end of the word.
6. Finally, we return the `count` variable, which represents the number of vowels in the input string.