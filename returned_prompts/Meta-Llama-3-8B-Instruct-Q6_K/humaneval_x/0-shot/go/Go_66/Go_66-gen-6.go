The function should sum up the ASCII values of all uppercase characters in the string. Here's how you can do it in Go:

```go
func Digitsum(x string) int {
    sum := 0
    for _, char := range x {
        if char >= 'A' && char <= 'Z' {
            sum += int(char - 'A' + 65)
        }
    }
    return sum
}
```

This function loops over each character in the string. If the character is uppercase (i.e., its ASCII value is between 'A' and 'Z'), it adds the ASCII value of the character minus the ASCII value of 'A' plus 65 to the sum. The ASCII value of 'A' minus 1 is used to calculate the sum because the ASCII value of 'A' is 65. The sum of the ASCII values of all uppercase characters is then returned. 