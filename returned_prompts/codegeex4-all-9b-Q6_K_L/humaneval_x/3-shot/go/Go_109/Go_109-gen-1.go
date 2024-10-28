
For the HasCloseElements function, the logic is straightforward. You iterate over each pair of numbers in the list and calculate their absolute difference. If any pair's difference is less than the threshold, you return true. If no such pair is found, you return false.
```go
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var distance float64 = math.Abs(numbers[i] - numbers[j])
            if distance < threshold {
                return true
            }
        }
    }
    return false
}
```

For the SeparateParenGroups function, you iterate over each character in the input string. If you encounter an opening parenthesis, you increment the current depth and add it to the current string. If you encounter a closing parenthesis, you decrement the current depth and add it to the current string. If the current depth is zero, it means you've closed all opened parentheses for a group, so you add the current string to the result and reset it. Finally, you return the result.
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
                current_string = make([]r