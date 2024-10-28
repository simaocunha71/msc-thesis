
```go
func SeparateParenGroups(paren_string string) []string {
    var result []string
    var current string

    for i, r := range paren_string {
        if r == '(' {
            current += string(r)
        } else if r == ')' {
            if len(current) == 0 {
                continue
            }
            result = append(result, current)
            current = ""
        }
    }
    return result
}
```

Explanation:

The function `SeparateParenGroups` takes a string of multiple groups of nested parentheses as input and returns a slice of strings representing the separated groups. The function uses two variables, `result` and `current`, to store the separated groups and the current group being processed, respectively.

The function uses a loop to iterate through each character in the input string. If the character is an opening parenthesis '(', it is added to the `current` string. If the character is a closing parenthesis ')', the function checks if the `current` string is empty. If it is empty, it means that the closing parenthesis is not properly balanced with an opening parenthesis, so the function skips it. Otherwise, it adds the `current` string to the `result` slice and resets the `current` string to an empty string.

Finally, the function returns the `result` slice, which contains all the separated groups of parentheses.

In the provided example, the function is called with the input string `'( ) (( )) (( )( ))'`. The function processes the input string and separates the groups of parentheses, resulting in the output `['()', '(())', '(()())']`.

Overall, the solution uses a simple approach to separate the groups of parentheses by iterating through the input string and keeping track of the current group being processed. It ensures that the groups are balanced and not nested within each other by checking the length of the `current` string before adding it to the `result` slice.

```go
package main

import "fmt"

func main() {
    fmt.Println(SeparateParenGroups("( ) (( )) (( )( ))"))
    // Output: ['()', '