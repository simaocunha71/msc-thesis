
In your first example, you're missing a return statement.
Also, you're using the wrong variable name. The variable should be named distance, not dist. You can simplify the code with the math.Dist function.

func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            dist := math.Abs(numbers[i] - numbers[j])
            if dist < threshold {
                return true
            }
        }
    }
    return false
}

In your second example, you're missing a return statement. You're also using the wrong variable name. The variable should be named result, not res. You can simplify the code with the strings.Builder type.

func SeparateParenGroups(paren_string string) []string {
    var result []string
    var current_string strings.Builder
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_string.WriteRune(c)
        } else if c == ')' {
            current_depth -= 1
            current_string.WriteRune(c)

            if current_depth == 0 {
                result = append(result, current_string.String())
                current_string.Reset()
            }
        }
    }
    return result
}

In your third example, you're missing a return statement. You're also using the wrong variable name. The variable should be named number, not num. You can