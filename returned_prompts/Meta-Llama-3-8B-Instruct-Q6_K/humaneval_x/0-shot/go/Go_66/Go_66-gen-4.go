```go
func Digitsum(x string) int {
    var sum int
    for _, v := range x {
        if v >= 'A' && v <= 'Z' {
            sum += int(v - 'A' + 65)
        }
    }
    return sum
}
```


*   We iterate through each character in the input string `x` using a `for` loop with a range.
*   For each character, we check if it is an uppercase letter using the condition `v >= 'A' && v <= 'Z'`. If it is, we add its ASCII value to the `sum` variable.
*   We calculate the ASCII value of the uppercase letter by subtracting the ASCII value of 'A' (65) and adding 65 to the character's ASCII value. This is because the ASCII values of uppercase letters range from 65 to 90, and subtracting 'A' (65) gives us the position of the letter in the alphabet (0-25), which can be used to calculate the ASCII value.
*   Finally, we return the `sum` variable, which contains the sum of the ASCII values of the uppercase characters in the input string.