```go
func Digitsum(x string) int {
    sum := 0
    for _, char := range x {
        if char >= 'A' && char <= 'Z' {
            sum += int(char)
        }
    }
    return sum
}
```
Explanation:
The function `Digitsum` takes a string `x` as input and returns the sum of the ASCII codes of the upper case characters in the string.

We initialize a variable `sum` to 0 to keep track of the sum of the ASCII codes.

We then iterate over each character in the string `x` using a range loop. For each character, we check if it is an upper case character by checking if its ASCII value is between 'A' (65) and 'Z' (90). If it is an upper case character, we add its ASCII value to the `sum`.

Finally, we return the `sum` at the end of the function.

This function works for the given examples and returns the expected results.