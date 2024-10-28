```
func Digitsum(x string) int {
    var sum int
    for _, char := range x {
        if char >= 'A' && char <= 'Z' {
            sum += int(char - 'A' + 65)
        }
    }
    return sum
}
```


The function takes a string as input and initializes a variable `sum` to 0. It then iterates over each character in the string using a range-based loop. For each character, it checks if the character is an uppercase letter by checking if its ASCII value falls within the range of 'A' to 'Z'. If the character is an uppercase letter, it adds the ASCII value of the character minus the ASCII value of 'A' plus 65 to the `sum`. This is because the ASCII values of uppercase letters are consecutive, with 'A' having a value of 65, 'B' having a value of 66, and so on.

Finally, the function returns the `sum` value.

This function can be used to calculate the sum of the upper characters only' ASCII codes in a string, as shown in the examples. For instance, `Digitsum("abAB")` would return 131, which is the sum of the ASCII codes of 'A' and 'B'. Similarly, `Digitsum("abcCd")` would return 67, which is the sum of the ASCII codes of 'C' and 'D'.