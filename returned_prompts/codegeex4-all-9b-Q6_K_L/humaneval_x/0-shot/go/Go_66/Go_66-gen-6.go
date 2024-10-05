You can solve this task using the following steps:

1. Initialize a variable to store the sum of the ASCII codes.
2. Iterate through each character in the string.
3. Check if the character is an uppercase letter by comparing its ASCII code with the ASCII codes of 'A' and 'Z'.
4. If the character is an uppercase letter, add its ASCII code to the sum.
5. Return the sum.

Here is the solution in Go:

```go
func Digitsum(x string) int {
    var sum int
    for _, char := range x {
        if char >= 'A' && char <= 'Z' {
            sum += int(char)
        }
    }
    return sum
}
```