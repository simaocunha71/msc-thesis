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
    result := ""
    for i := 0; i < len(a); i++ {
        if string(a[i]) == string(b[i]) {
            result += "0"
        } else {
            result += "1"
        }
    }
    return result
}

func main() {
    fmt.Println(StringXor("010", "110")) // Output: 100
}
```

This program defines a function `StringXor` that takes two strings `a` and `b` as input. The function then iterates over the characters of the two strings, and for each pair of characters, it checks if they are the same. If they are the same, it adds a "0" to the result string; if they are different, it adds a "1". Finally, the function returns the result string.

In the `main` function, we call `StringXor` with the inputs "010" and "110", and print the result to the console. The output is "100", which is the binary XOR of the two input strings.