```go
func Digitsum(x string) int {
    sum := 0
    for _, c := range x {
        if unicode.IsUpper(c) {
            sum += int(c)
        }
    }
    return sum
}
```

Explanation:
The `Digitsum` function takes a string `x` as input and returns the sum of the ASCII codes of the upper case characters in the string.

The function uses a `for` loop to iterate over each character `c` in the string `x`. The `unicode.IsUpper` function is used to check if the character is an upper case letter. If it is, the ASCII code of the character is added to the `sum` variable.

Finally, the `sum` variable is returned as the result. The `int(c)` conversion is used to convert the character to its ASCII code, which is an `int` type.

Note that this function does not handle non-ASCII characters, such as accented letters or non-Latin characters. If you need to handle such characters, you may need to use a more sophisticated approach, such as using a regular expression to match upper case letters.