
Your first function is correct, but there's room for optimization.
The inner loop starts at i+1, so you can start the outer loop at 0 and the inner loop at i. This saves one comparison per iteration of the inner loop, so it runs a bit faster.
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}

Your second function has some issues:

You're not ignoring spaces in the input string. You should use strings.ReplaceAll to remove them.
You're not handling nested parentheses correctly. You need to keep track of the current depth and only add parentheses to the current_string when the depth is zero.
You're not handling the case where there are no parentheses in the input string. You should return an empty slice in that case.

Here's a corrected version of the function:
func SeparateParenGroups(paren_string string) []string {
    paren_string = strings.ReplaceAll(paren_string, " ", "")
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth++
            current_string = append(current_string, c)
        } else if c == ')' {
            current_depth--
            current_string = append(current_string, c)
            if current_depth == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        }
    }
    return result
}

Your third function is correct, but it can be simplified:
func TruncateNumber(number float64) float64 {
    return math.Mod(number, 1)
}

Your fourth function has some issues:

You're not ignoring spaces in the input string. You should use strings.ReplaceAll to remove them.
You're not handling the case where there