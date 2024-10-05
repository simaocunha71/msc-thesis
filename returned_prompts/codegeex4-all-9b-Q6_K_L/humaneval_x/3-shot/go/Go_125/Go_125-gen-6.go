
I'll go over the three of them.

HasCloseElements

Your code seems correct, but it could be optimized. You're iterating over the same items over and over again. What you can do is sort the numbers array first, then do a single pass to check if two consecutive numbers are smaller than the threshold. This way, you only need to iterate over the array once. Here's how you can do it:
func HasCloseElements(numbers []float64, threshold float64) bool {
    sorted := make([]float64, len(numbers))
    copy(sorted, numbers)
    sort.Float64s(sorted)

    for i := 1; i < len(sorted); i++ {
        if sorted[i] - sorted[i-1] < threshold {
            return true
        }
    }
    return false
}

SeparateParenGroups

Your code seems correct, but there's a potential issue. If the input string doesn't contain any parentheses, your code will return an empty list of strings. However, according to the problem description, you should return 0 if the input string doesn't contain any parentheses. You can modify your code to return 0 in that case:
func SeparateParenGroups(paren_string string) interface{} {
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

    if len(result) == 0 {
        return 0
    }

    return result
}

TruncateNumber

Your code seems correct, but there's a potential issue. If the input number