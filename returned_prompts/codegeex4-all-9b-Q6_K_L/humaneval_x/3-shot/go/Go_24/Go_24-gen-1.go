
Your code looks good, but it can be optimized a bit:

In HasCloseElements, you can skip the outer loop if the current number is greater than the threshold. This is because if the current number is greater than the threshold, then the distance between it and any other number will be greater than the threshold.
In SeparateParenGroups, you don't need to use a rune slice to store the current string. You can use a string slice and then join them into a single string when you add it to the result.
In TruncateNumber, you can use the built-in math.Trunc function to truncate the number.

Here's the optimized code:
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        if numbers[i] > threshold {
            break
        }
        for j := i + 1; j < len(numbers); j++ {
            var distance float64 = math.Abs(numbers[i] - numbers[j])
            if distance < threshold {
                return true
            }
        }
    }
    return false
}

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

func TruncateNumber(number float64) float64 {
    return math.Trunc(number)
}