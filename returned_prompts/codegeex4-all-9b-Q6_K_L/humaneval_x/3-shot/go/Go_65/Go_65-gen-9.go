
Your solution for Q1 is correct, but it is not optimal for performance. You are iterating over the slice twice, and in fact, it is possible to do it in a single pass. You can achieve this by keeping track of the current depth of parentheses and adding the characters to the current string only when the depth is positive. This way, you don't need to check for the depth in each iteration, which can be a performance bottleneck.
Here is an optimized version of your solution:
func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
        } else if c == ')' {
            current_depth -= 1
        }

        if current_depth > 0 {
            current_string = append(current_string, c)
        }
    }

    if len(current_string) > 0 {
        result = append(result, string(current_string))
    }

    return result
}

Your solution for Q2 is correct, but it can be optimized by using a loop instead of a recursive call. This way, you don't have to create a new string in each iteration, which can be a performance bottleneck.
Here is an optimized version of your solution:
func CircularShift(x int, shift int) string {
    s := strconv.Itoa(x)
    if len(s) <= shift {
        return reverse(s)
    }

    return s[shift:] + s[:shift]
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

Your solution for Q3 is correct, but it can