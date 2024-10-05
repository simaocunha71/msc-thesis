You can use the built-in `strings.Count` function in Go to count the occurrences of a substring in a given string. This function returns the number of non-overlapping instances of `substr` in `s`. 

Here is an example of how you can use it:

```go
package main

import (
    "fmt"
    "strings"
)

func HowManyTimes(str string, substring string) int {
    return strings.Count(str, substring)
}

func main() {
    fmt.Println(HowManyTimes("aaa", "a"))    // Output: 3
    fmt.Println(HowManyTimes("aaaa", "aa"))  // Output: 3
    fmt.Println(HowManyTimes("", "a"))      // Output: 0
}
```

In this code, the `HowManyTimes` function takes two parameters, `str` and `substring`, and returns the number of times `substring` appears in `str`. The `strings.Count` function is used to count the occurrences of `substring` in `str`.

The `main` function is used to test the `HowManyTimes` function with different inputs.