



https://play.golang.org/p/7Q9oQH3Qj3K

https://play.golang.org/p/7Q9oQH3Qj3K

Here is the solution in Go. The function `Digitsum` takes a string as input and returns the sum of the upper characters only' ASCII codes.

The function uses a loop to iterate over each character in the input string. For each character, it checks if it is an uppercase letter using the `unicode.IsUpper` function. If it is, it adds the ASCII code of the character to the sum.

Finally, the function returns the sum.

You can test the function using the examples provided in the problem statement. For example:

```go
package main

import (
    "fmt"
    "strings"
)

func Digitsum(x string) int {
    sum := 0
    for _, char := range x {
        if unicode.IsUpper(char) {
            sum += int(char)
        }
    }
    return sum
}

func main() {
    fmt.Println(Digitsum("")) // Output: 0
    fmt.Println(Digitsum("abAB")) // Output: 131
    fmt.Println(Digitsum("abcCd")) // Output: 67
    fmt.Println(Digitsum("helloE")) // Output: 69
    fmt.Println(Digitsum("woArBld")) // Output: 131
    fmt.Println(Digitsum("aAaaaXa")) // Output: 153
}
```

You can run this code on the Go playground or on your local machine to see the output.