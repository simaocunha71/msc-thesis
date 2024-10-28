    // Initialize length counter
    var length int
    // Loop through each character in the string
    for i := 0; i < len(str); i++ {
        // Increment length counter
        length++
    }
    // Return length
    return length
}

func main() {
    fmt.Println(Strlen(""))  // Output: 0
    fmt.Println(Strlen("abc"))  // Output: 3
}

Answer:
Here is a simple Go program that counts the length of a given string.

```go
package main

import (
    "fmt"
)

// Return length of given string
func Strlen(str string) int {
    // Initialize length counter
    var length int
    // Loop through each character in the string
    for i := 0; i < len(str); i++ {
        // Increment length counter
        length++
    }
    // Return length
    return length
}

func main() {
    fmt.Println(Strlen(""))  // Output: 0
    fmt.Println(Strlen("abc"))  // Output: 3
}
```

The function `Strlen` takes a string as an argument and initializes a variable `length` to 0. Then it loops over each character in the string, incrementing `length` for each character. Finally, it returns the total length of the string.

The `main` function calls `Strlen` with an empty string and a string with length 3, and prints the results. The output will be `0` and `3`, respectively.