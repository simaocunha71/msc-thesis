```
func Digitsum(x string) int {
    var sum int
    for _, v := range x {
        if unicode.IsUpper(rune(v)) {
            sum += int(v)
        }
    }
    return sum
}
```
This solution uses the `unicode.IsUpper` function to check if a character is uppercase. If it is, it converts the character to an integer using the `int()` function and adds it to the sum. Finally, it returns the sum. The `_` variable is a common convention in Go for an unused variable. In this case, it's used to ignore the index returned by the `range` keyword, since we're only interested in the value of each character. The `rune` type is used to convert the character to a Unicode code point, which can be used with the `unicode.IsUpper` function.