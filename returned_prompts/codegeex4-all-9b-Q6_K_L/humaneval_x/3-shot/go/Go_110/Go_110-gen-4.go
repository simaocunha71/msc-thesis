
HasCloseElements
Your code is almost correct, but you have a bug in the first for loop condition. You are checking the length of numbers for every iteration, but the length does not change while you are iterating. You should move the length check outside of the loop.
Here is the corrected code:
func HasCloseElements(numbers []float64, threshold float64) bool {
    n := len(numbers)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            var distance float64 = math.Abs(numbers[i] - numbers[j])
            if distance < threshold {
                return true
            }
        }
    }
    return false
}

SeparateParenGroups
Your code is correct, but it can be optimized. You don't need to check if the current depth is zero after each iteration. You can check it after the inner loop and if it is zero, you can append the current string to the result and reset it.
Here is the optimized code:
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

TruncateNumber
Your code is correct, but you can simplify it by using the