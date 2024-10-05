```go
package main
import (
    "strconv"
    "strings"
)

// Return a string containing space-delimited numbers starting from 0 upto n inclusive.
// >>> StringSequence(0)
// '0'
// >>> StringSequence(5)
// '0 1 2 3 4 5'
func StringSequence(n int) string {
    var result strings.Builder
    for i := 0; i <= n; i++ {
        result.WriteString(strconv.Itoa(i))
        if i < n {
            result.WriteString(" ")
        }
    }
    return result.String()
}

func main() {
    println(StringSequence(0))  // Output: 0
    println(StringSequence(5))  // Output: 0 1 2 3 4 5
}
```



Explanation:

*   We use a `strings.Builder` to efficiently build the output string.
*   We iterate from 0 to `n` using a for loop.
*   Inside the loop, we use `strconv.Itoa(i)` to convert the integer `i` to a string and append it to the `result` builder.
*   If `i` is less than `n`, we append a space to the builder using `result.WriteString(" ")`.
*   After the loop, we return the string representation of the `result` builder using `result.String()`.
*   In the `main` function, we test the `StringSequence` function with inputs 0 and 5, and print the results using `println`. The output matches the expected results.