
// Remove all spaces
paren_string = strings.ReplaceAll(paren_string, " ", "")

// Initialize an empty list to store the result
result := make([]string, 0)

// Initialize a stack to keep track of parentheses
stack := make([]rune, 0)

// Initialize a temporary string to store the current group
temp := ""

// Traverse the input string
for _, c := range paren_string {
    // If the character is an open brace, push it into the stack
    if c == '(' {
        stack = append(stack, c)
    } else if c == ')' {
        // If the character is a closed brace, pop from the stack and add it to the temporary string
        if len(stack) > 0 {
            stack = stack[:len(stack)-1]
            temp += string(c)
        }
    }

    // If the stack becomes empty, we have found a balanced group
    if len(stack) == 0 {
        // Add the group to the result list
        result = append(result, temp)
        // Reset the temporary string
        temp = ""
    }
}

// Return the result list
return result
}
```
This function uses a stack to keep track of the parentheses. It iterates over the input string and pushes open parentheses onto the stack. When a closed parenthesis is encountered, it pops from the stack and adds it to the current group. When the stack becomes empty, we have found a balanced group. This process is repeated until all parentheses are processed. The result is a list of balanced groups.

Please note that this function assumes that the input string is well-formed and does not contain any invalid characters.

This function also does not handle nested parentheses as per your question. If you want to handle nested parentheses, you would need to modify the function to keep track of the depth of the parentheses and only consider a group as a separate one when the depth is 0.

Here is a modified version of the function that handles nested parentheses:

```go
func SeparateParenGroups(paren_string string) []string {
    paren_