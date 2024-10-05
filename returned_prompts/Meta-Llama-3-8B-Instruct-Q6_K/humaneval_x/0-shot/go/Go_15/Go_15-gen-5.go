```go
package main
import (
    "fmt"
    "strconv"
)

// Return a string containing space-delimited numbers starting from 0 upto n inclusive.
// >>> StringSequence(0)
// '0'
// >>> StringSequence(5)
// '0 1 2 3 4 5'
func StringSequence(n int) string {
    result := ""
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return result[:len(result)-1] // Remove the trailing space
}

func main() {
    fmt.Println(StringSequence(0))  // Output: 0
    fmt.Println(StringSequence(5))  // Output: 0 1 2 3 4 5
}
```
In this Go code, we define a function `StringSequence` that generates a string containing space-delimited numbers from 0 to `n` inclusive. The function uses a `for` loop to iterate over the numbers and concatenates each number to the `result` string using `strconv.Itoa(i)`. After the loop, we return the `result` string with the trailing space removed using `result[:len(result)-1]`.

In the `main` function, we test the `StringSequence` function with `n = 0` and `n = 5` and print the results to the console.

Output:
```
0
0 1 2 3 4 5
```
This code demonstrates a simple and efficient way to generate a string sequence of numbers in Go.