
Here's a solution to the problem:

You need to iterate over the parentheses in the string.
If you find an opening parenthesis, you increment a counter.
If you find a closing parenthesis, you decrement the counter.
If the counter reaches zero, you've found a complete group of parentheses. You add it to your result and reset the counter.
If the counter is negative at any point, you've made a mistake and need to return an error.

Here's the code:

```go
func SeparateParenGroups(paren_string string) ([]string, error) {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_string = append(current_string, c)
        } else if c == ')' {
            current_depth -= 1
            current_string = append(current_string, c)

            if current_depth == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            } else if current_depth < 0 {
                return nil, errors.New("Unbalanced parentheses")
            }
        }
    }

    if current_depth != 0 {
        return nil, errors.New("Unbalanced parentheses")
    }

    return result, nil
}
```

This function will return a slice of strings containing the groups of parentheses, or an error if the parentheses are not balanced.