
Your solution for SeparateParenGroups has a bug. You need to handle the case when there are spaces in the string. Here is a corrected version of your code:

func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' && !isSpace(current_string) {
            current_depth += 1
            current_string = append(current_string, c)
        } else if c == ')' && !isSpace(current_string) {
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

func isSpace(s []rune) bool {
    for _, c := range s {
        if c != ' ' {
            return false
        }
    }
    return true
}

Your solution for TruncateNumber is correct.

Your solution for TriangleArea is correct.