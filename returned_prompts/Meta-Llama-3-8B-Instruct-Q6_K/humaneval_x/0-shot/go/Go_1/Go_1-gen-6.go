The function can be implemented by iterating over the input string and keeping track of the number of open and close parentheses. When the number of open parentheses is greater than the number of close parentheses, it means that a new group is starting, and we should add the current group to the result and reset the counters. Here is a sample implementation in Go:

```go
func SeparateParenGroups(paren_string string) []string {
    result := []string{}
    curr := ""
    open, close := 0, 0

    for _, c := range paren_string {
        if c == '(' {
            open++
        } else {
            close++
        }
        curr += string(c)

        if open == close {
            result = append(result, curr[:len(curr)-1])
            curr = ""
            open, close = 0, 0
        }
    }

    return result
}
```

The function iterates over the input string. For each character, it increments the corresponding counter (open or close) and adds the character to the current group. When the number of open parentheses equals the number of close parentheses, it means that a group has been fully processed, and we add the current group to the result, reset the counters and the current group. The function returns the list of processed groups. The sample output for the input `"( ) (( )) (( )( ))"` is `["()", "(())", "(()())"]`.