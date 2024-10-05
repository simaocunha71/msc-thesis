```go
func CountUpper(s string) int {
    count := 0
    for i, c := range s {
        if i%2 == 0 && strings.ToUpper(string(c)) == string(c) {
            count++
        }
    }
    return count
}
```

In this solution, we iterate over the string `s` using a range-based for loop. For each character `c` at index `i`, we check if `i` is even (`i%2 == 0`) and if the character is an uppercase vowel (`strings.ToUpper(string(c)) == string(c)`). If both conditions are true, we increment the `count` variable. Finally, we return the `count`. The `strings.ToUpper` function is used to convert the character to uppercase and compare it with the original character. The `string(c)` conversion is used to convert the character to a string, which is required for the comparison. The `strings.ToUpper` function is used to convert the string to uppercase, which is then compared with the original string. If they are equal, it means the character is an uppercase vowel. The count is incremented and the loop continues until all characters have been processed. The final count is returned as the result.