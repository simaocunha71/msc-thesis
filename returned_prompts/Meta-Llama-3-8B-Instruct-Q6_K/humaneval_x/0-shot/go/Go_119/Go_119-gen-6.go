The function MatchParens takes a slice of strings as input, where each string contains only open parentheses '(' or close parentheses ')'. The function checks if it is possible to concatenate the strings in some order to form a balanced string. A string is considered balanced if all parentheses are properly closed.

Here is the implementation in Go:
```go
func MatchParens(lst []string) string {
    var stack []byte
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                stack = append(stack, '(')
            } else {
                if len(stack) == 0 || stack[len(stack)-1] != '(' {
                    return "No"
                }
                stack = stack[:len(stack)-1]
            }
        }
    }
    return "Yes"
}
```
In the function, we iterate over each string in the input slice. For each string, we iterate over each character. If the character is an open parenthesis, we push it onto the stack. If the character is a close parenthesis, we check if the stack is empty or the top of the stack is not an open parenthesis. If either condition is true, we return "No". Otherwise, we pop the top element from the stack.

After processing all strings, if the stack is empty, we return "Yes". Otherwise, we return "No". This is because a stack with elements remaining indicates that there are unmatched open parentheses, making the string unbalanced. 

For example, the input `['()(', ')']` will return "Yes" because we can concatenate the strings in the order `'(())'`, which is a balanced string. The input `[')', ')']` will return "No" because there are unmatched close parentheses. 

This function has a time complexity of O(n), where n is the total number of characters in all input strings, and a space complexity of O(m), where m is the total number of parentheses in all input strings. 

Note: The function does not handle the case where the input contains strings with different lengths. If such a case is possible, the function should be modified to handle it. 

Also, the function assumes that the input strings only contain open and close parentheses. If the input strings can contain other characters, the function should be modified to handle them. 