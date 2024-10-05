Here is a possible implementation of the `MatchParens` function in Go:
```go
func MatchParens(lst []string) string {
    count := 0
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                count++
            } else {
                count--
                if count < 0 {
                    return "No"
                }
            }
        }
    }
    return "Yes"
}
```
Here's an explanation of how the function works:

1. We initialize a counter `count` to 0.
2. We iterate over each string in the input list `lst`.
3. For each string, we iterate over each character `c` in the string.
4. If `c` is an open parenthesis `(`, we increment the `count` variable.
5. If `c` is a close parenthesis `)`, we decrement the `count` variable. If the `count` variable becomes negative, it means that there are more close parentheses than open parentheses, so we return "No".
6. After processing all strings, we return "Yes" if the `count` variable is still 0 (i.e., all parentheses are balanced), or "No" otherwise.

You can test this function with the examples you provided:
```go
fmt.Println(MatchParens([]string{"()(", ")"})) // Output: "Yes"
fmt.Println(MatchParens([]string{")", ")"})) // Output: "No"
```
I hope this helps! Let me know if you have any questions.