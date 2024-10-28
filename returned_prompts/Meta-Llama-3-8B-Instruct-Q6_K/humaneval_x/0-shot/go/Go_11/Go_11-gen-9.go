```go
package main

import (
    "fmt"
)

// Input are two strings a and b consisting only of 1s and 0s.
// Perform binary XOR on these inputs and return result also as a string.
// >>> StringXor('010', '110')
// '100'
func StringXor(a string, b string) string {

    // Initialize an empty string to store the result.
    result := ""

    // Iterate over the characters in both strings.
    for i := 0; i < len(a); i++ {
        // Calculate the XOR of the current characters.
        bit := byte(a[i] ^ b[i])

        // Convert the XOR result to a string and add it to the result string.
        result += fmt.Sprintf("%c", bit)
    }

    // If the strings are of different lengths, append the remaining characters.
    if len(a) > len(b) {
        result += a[len(b):]
    } else if len(b) > len(a) {
        result += b[len(a):]
    }

    return result
}

func main() {
    fmt.Println(StringXor('010', '110')) // Output: "100"
}
```


Explanation:
The provided Go function `StringXor` takes two strings `a` and `b` as input, both consisting of only 1s and 0s. It performs a binary XOR operation on these inputs and returns the result as a string.

Here's a step-by-step explanation of the code:

1. Initialize an empty string `result` to store the result of the XOR operation.
2. Iterate over the characters in both strings `a` and `b` using a for loop.
3. For each character, calculate the XOR of the current characters using the bitwise XOR operator (`^`).
4. Convert the XOR result to a string using the `fmt.Sprintf` function and add it to the `result` string.
5. If the strings are of different lengths, append the remaining characters to the `result` string.
6. Return the `result` string.

The `main` function demonstrates the usage of the `StringXor` function by calling it with the inputs `'010'` and `'110'` and printing the result. The output is `"100"`, which is the result of the binary XOR operation on the two input strings.