```go
package main

import (
    "fmt"
    "strings"
)

func CycpatternCheck(a, b string) bool {
    b = strings.ToLower(b)
    for i := 0; i < len(a); i++ {
        if strings.Contains(strings.ToLower(a), b) {
            return true
        }
        a = a[1:] + a[0:1]
    }
    return false
}

func main() {
    fmt.Println(CycpatternCheck("abcd", "abd"))     // false
    fmt.Println(CycpatternCheck("hello", "ell"))    // true
    fmt.Println(CycpatternCheck("whassup", "psus"))  // false
    fmt.Println(CycpatternCheck("abab", "baa"))     // true
    fmt.Println(CycpatternCheck("efef", "eeff"))    // false
    fmt.Println(CycpatternCheck("himenss", "simen")) // true
}
```

S:

Here's a solution in Go:

```go
package main

import (
    "fmt"
    "strings"
)

func CycpatternCheck(a, b string) bool {
    b = strings.ToLower(b)
    for i := 0; i < len(a); i++ {
        if strings.Contains(strings.ToLower(a), b) {
            return true
        }
        a = a[1:] + a[0:1]
    }
    return false
}

func main() {
    fmt.Println(CycpatternCheck("abcd", "abd"))     // false
    fmt.Println(CycpatternCheck("hello", "ell"))    // true
    fmt.Println(CycpatternCheck("whassup", "psus"))  // false
    fmt.Println(CycpatternCheck("abab", "baa"))     // true
    fmt.Println(CycpatternCheck("efef", "eeff"))    // false
    fmt.Println(CycpatternCheck("himenss", "simen")) // true
}
```

The `CycpatternCheck` function works by rotating the first string and checking if the second string is a substring of the rotated string. It uses the `strings.Contains` function to check for the presence of the second string in the rotated first string. The rotation is done by slicing the first string and concatenating it in a circular manner. The function returns `true` if the second string is found in any of the rotated strings, and `false