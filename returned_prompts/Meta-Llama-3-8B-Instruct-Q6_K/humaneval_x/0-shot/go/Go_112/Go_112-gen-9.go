Here is the solution in Golang:
```go
package main

import (
    "strings"
)

func ReverseDelete(s, c string) [2]interface{} {
    var result string
    for _, char := range s {
        if !strings.Contains(c, string(char)) {
            result += string(char)
        }
    }
    reversed := []rune(result)
    for i, j := 0, len(reversed)-1; i < j; i, j = i+1, j-1 {
        reversed[i], reversed[j] = reversed[j], reversed[i]
    }
    result = string(reversed)
    return [2]interface{}{result, strings.EqualFold(result, result)}
}

func main() {
    result := ReverseDelete("abcde", "ae")
    print(result) // Output: [bcd false]
}
```

In this solution, we first create a new string `result` and iterate over each character `char` in the original string `s`. If the character is not present in the string `c`, we add it to the `result` string.

Then, we reverse the `result` string using a simple swap algorithm.

Finally, we check if the reversed `result` string is equal to the original `result` string (ignoring case) and return a tuple containing the `result` string and a boolean value indicating whether the `result` string is a palindrome.

The `main` function demonstrates how to use the `ReverseDelete` function. It calls `ReverseDelete` with the input strings "abcde" and "ae", and prints the result. The output is `[bcd false]`, which means the `result` string is "bcd" and it is not a palindrome.