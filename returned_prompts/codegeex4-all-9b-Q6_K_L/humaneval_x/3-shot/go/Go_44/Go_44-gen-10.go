
Let's start with the first function `SeparateParenGroups`. The logic seems correct, but there are a few issues:

1. You're not handling the case where the input string has spaces. You should skip those.
2. You're not handling the case where the input string has parentheses that are not properly balanced. You should return an error in that case.

Here's an updated version of the function:

```go
func SeparateParenGroups(paren_string string) ([]string, error) {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == ' ' {
            continue
        } else if c == '(' {
            current_depth += 1
            current_string = append(current_string, c)
        } else if c == ')' {
            current_depth -= 1
            current_string = append(current_string, c)

            if current_depth == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        } else {
            return nil, fmt.Errorf("Invalid character: %c", c)
        }
    }

    if current_depth != 0 {
        return nil, fmt.Errorf("Unbalanced parentheses")
    }

    return result, nil
}
```

Now let's move on to the second function `TruncateNumber`. The logic is correct, but you're not handling the case where the input number is less than 1. In that case, you should return 0. Here's an updated version of the function:

```go
func TruncateNumber(number float64) float64 {
    if number < 1 {
        return 0
    }
    return math.Mod(number, 1)
}
```

Finally, let's move on to the third function `ChangeBase`. The logic is correct, but you're not handling the case where the base is not between 2 and 9. In that case, you should return an error.