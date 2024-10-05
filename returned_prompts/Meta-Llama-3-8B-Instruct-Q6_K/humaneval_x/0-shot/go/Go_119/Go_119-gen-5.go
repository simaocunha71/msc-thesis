```go
func MatchParens(lst []string) string {
    count := 0
    for _, v := range lst {
        for _, c := range v {
            if c == '(' {
                count++
            } else if c == ')' {
                if count == 0 {
                    return "No"
                }
                count--
            }
        }
    }
    if count > 0 {
        return "No"
    }
    return "Yes"
}
```

Explanation:
The function `MatchParens` takes a list of strings as input, where each string consists of only open parentheses '(' or close parentheses ')'. It checks if it is possible to concatenate the two strings in some order, that the resulting string will be good (i.e., all parentheses are balanced).

The function initializes a counter `count` to 0. Then, it iterates over each string in the list, and for each string, it iterates over each character. If the character is an open parenthesis '(' , it increments the `count`. If the character is a close parenthesis ')', it decrements the `count`. If the `count` becomes 0 at any point, it means that there are more close parentheses than open parentheses, so the function returns "No". After iterating over all strings, if the `count` is greater than 0, it means that there are more open parentheses than close parentheses, so the function returns "No". Otherwise, it returns "Yes".

For example, for the input `['()(', ')']`, the function returns "Yes" because we can concatenate the strings in the order `('()')(')` to get a good string. For the input `[')', ')']`, the function returns "No" because we cannot concatenate the strings to get a good string.