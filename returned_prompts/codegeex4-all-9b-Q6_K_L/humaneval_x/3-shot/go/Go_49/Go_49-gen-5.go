
Your first function looks good. You have the right idea of using two nested loops to check all pairs of numbers.

Your second function is almost correct, but it needs to handle the case where the input string doesn't have any parentheses. In this case, your function would return an empty list instead of returning the input string as a single-element list. Here's a corrected version:
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

    if len(current_string) > 0 {
        result = append(result, string(current_string))
    }

    return result
}

Your third function is correct, but it can be simplified. You don't need to use a loop to calculate the result. You can just return the result of the expression (n % 2 == 1) ? p * p % n : 1. Here's a simplified version:
func Modp(n int, p int) int {
    return (n % 2 == 1) ? p * p % n : 1
}