```go
package main

import (
    "fmt"
    "strings"
)

func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, bracket := range strings.Split(brackets, "") {
        switch bracket {
        case "<":
            stack = append(stack, bracket)
        case ">":
            if len(stack) == 0 || stack[len(stack)-1] != '<' {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}

func main() {
    fmt.Println(CorrectBracketing("<"))  // false
    fmt.Println(CorrectBracketing("<>")) // true
    fmt.Println(CorrectBracketing("<<><>>")) // true
    fmt.Println(CorrectBracketing("><<") ) // false
}
```

This program defines a function `CorrectBracketing` that takes a string of brackets as input and returns a boolean indicating whether every opening bracket has a corresponding closing bracket.

The function uses a stack data structure to keep track of the opening brackets that have not yet been closed. It iterates over the input string, and for each character:

- If the character is an opening bracket ('<'), it pushes it onto the stack.
- If the character is a closing bracket ('>'), it checks if the stack is empty or if the top of the stack does not match the closing bracket. If either condition is true, it returns `false`. Otherwise, it pops the opening bracket from the stack.

Finally, it returns `true` if the stack is empty (i.e., all opening brackets have been closed) and `false` otherwise.

The `main` function tests the `CorrectBracketing` function with several examples and prints the results.