Here is the solution in Go:

```go
func OddCount(lst []string) []string {
    result := make([]string, len(lst))
    for i, str := range lst {
        count := 0
        for _, c := range str {
            if c % 2 != 0 {
                count++
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %d in the str%dng %d of the %dput.", count, i+48, i+48, i+48)
    }
    return result
}
```

This function iterates over each string in the input list. For each string, it counts the number of odd digits. Then, it constructs a string with the count, the number of the string (1-indexed), and the number of the string again. The number of the string is converted to a character by adding the ASCII value of '0' to the number. The result is a list of strings, each describing the number of odd digits in the corresponding input string. The function returns this list. 

For example, if the input is `["1234567"]`, the function will return `["the number of odd elements 4 in the string 7 of the input."].` If the input is `["3", "11111111"]`, the function will return `["the number of odd elements 1 in the string 3 of the input.", "the number of odd elements 8 in the string 11 of the input."]`. 

The `fmt.Sprintf` function is used to construct the output string. The `%d` format specifier is used to insert the count and the number of the string into the string. The `i+48` expression is used to convert the number of the string to a character. This is because the ASCII values of '1' through '9' are 49 through 57, respectively. The `i+48` expression adds the correct ASCII value to the number of the string to get the corresponding character.  The `%dput` format specifier is used to insert the number of the string into the string again. 

The function returns the list of output strings. 

This function assumes that the input list is not empty and that each string in the list consists only of digits. If these assumptions are not valid, the function may not work correctly. 

This function uses the `range` keyword to iterate over the input list and the strings in the list. It