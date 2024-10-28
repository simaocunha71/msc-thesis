```go
func FixSpaces(text string) string {
    var result strings.Builder
    var count int
    for _, char := range text {
        if char == ' ' {
            count++
            if count > 2 {
                result.WriteString "-"
            } else {
                result.WriteString "_"
            }
        } else {
            result.WriteString string(char)
            count = 0
        }
    }
    return result.String()
}
```
Explanation:

The function `FixSpaces` takes a string `text` as input and returns a new string with the spaces replaced as per the given rules.

The function uses a `strings.Builder` to efficiently build the resulting string.

We iterate over each character `char` in the input string `text`. If the character is a space `' '`, we increment the `count` variable. If `count` is greater than 2, we append a `-` to the result string, otherwise we append an underscore `_`. If the character is not a space, we simply append it to the result string and reset the `count` to 0.

Finally, we return the resulting string by calling the `String` method on the `strings.Builder`. This function is efficient because it uses a buffer to store the characters and avoids unnecessary memory allocations.