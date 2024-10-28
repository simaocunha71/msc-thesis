Here is the solution:
```go
import (
    "strings"
)

// For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
// >>> FlipCase('Hello')
// 'hELLO'
func FlipCase(str string) string {
    result := ""
    for _, c := range str {
        if strings.ToLower(string(c)) == string(c) {
            result += strings.ToUpper(string(c))
        } else {
            result += strings.ToLower(string(c))
        }
    }
    return result
}
```


Explanation:
The `FlipCase` function takes a string as input and returns a new string where all lowercase characters are flipped to uppercase and vice versa.

We use a `for` loop to iterate over each character `c` in the input string `str`. For each character, we check if it is a lowercase character by comparing it with its lowercase equivalent using the `strings.ToLower` function. If it is a lowercase character, we convert it to uppercase using the `strings.ToUpper` function and add it to the result string. If it is an uppercase character, we convert it to lowercase using the `strings.ToLower` function and add it to the result string.

Finally, we return the resulting string.

Example usage:
```go
func main() {
    str := "Hello"
    result := FlipCase(str)
    fmt.Println(result) // Output: "hELLO"
}
```


Note that this implementation assumes that the input string only contains ASCII characters. If the input string contains non-ASCII characters, additional handling may be required.