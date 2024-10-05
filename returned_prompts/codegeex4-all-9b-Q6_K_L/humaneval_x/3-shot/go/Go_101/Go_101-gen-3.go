
For the first problem, you can use the following code:
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

For the second problem, you can use the following code:
func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := ""
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_string += string(c)
        } else if c == ')' {
            current_depth -= 1
            current_string += string(c)

            if current_depth == 0 {
                result = append(result, current_string)
                current_string = ""
            }
        }
    }
    return result
}

For the third problem, you can use the following code:
func TruncateNumber(number float64) float64 {
    return math.Mod(number, 1)
}

For the fourth problem, you can use the following code:
func WordsString(s string) []string {
    return strings.Split(strings.ReplaceAll(s, ",", " "), " ")
}