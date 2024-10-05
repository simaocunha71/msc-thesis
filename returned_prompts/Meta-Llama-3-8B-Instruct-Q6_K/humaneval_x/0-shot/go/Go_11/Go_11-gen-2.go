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
        if a[i] == b[i] {
            result += "0"
        } else {
            result += "1"
        }
    }
    return result
}

func main() {
    fmt.Println(StringXor("010", "110"))
}
```

Output:
```
100
```

Explanation:
The function `StringXor` takes two strings `a` and `b` as input, which consist of 1s and 0s. It performs a binary XOR operation on these inputs and returns the result as a string. 

The XOR operation is performed by iterating over the input strings and comparing each character. If the characters at the current position in both strings are the same, the result string is appended with "0". If the characters are different, "1" is appended to the result string.

The `main` function demonstrates the usage of `StringXor` by calling it with the inputs "010" and "110", and printing the result. The output is "100", which is the binary XOR of "010" and "110". 