
The first function is correct and efficient. The time complexity is O(n^2) which is acceptable for small inputs.

The second function is almost correct, but it does not handle the case when the input string contains spaces. To fix this, you can add a check for spaces and skip them while parsing the string.

Here is the corrected version of the function:

```go
func SeparateParenGroups(paren_string string) []string {
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
            }
        }
    }
    return result
}
```

The third function is also correct. The time complexity is O(n) which is efficient for large inputs.

The fourth function is incorrect. The largest divisor of a number is not always the number itself. For example, the largest divisor of 15 is 5, not 15. To fix this, you can start the loop from n/2 and go down to 1. Here is the corrected version of the function:

```go
func LargestDivisor(n int) int {
    for i := n / 2; i >= 1; i-- {
        if n % i == 0 {
            return i
        }
    }
    return 0
}
```