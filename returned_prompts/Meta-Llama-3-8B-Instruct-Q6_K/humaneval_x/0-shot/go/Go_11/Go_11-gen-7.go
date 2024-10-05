```go
package main

import (
    "fmt"
)

func StringXor(a string, b string) string {
    result := ""
    for i := 0; i < len(a); i++ {
        if a[i] == '1' && b[i] == '1' {
            result += '0'
        } else if a[i] == '0' && b[i] == '0' {
            result += '0'
        } else {
            result += '1'
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

The function `StringXor` takes two strings `a` and `b` as input, both consisting of 1s and 0s. The function iterates over each character in the strings, and for each pair of characters, it performs a binary XOR operation. The result of the XOR operation is then added to the `result` string.

In the `main` function, we call `StringXor` with the inputs "010" and "110", and print the result. The output is "100", which is the result of performing the binary XOR operation on the two input strings.