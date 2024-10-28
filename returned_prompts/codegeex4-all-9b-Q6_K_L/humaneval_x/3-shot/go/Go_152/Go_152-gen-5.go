
1) Your HasCloseElements function is correct. Here is the function for you:
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

2) Your SeparateParenGroups function is correct. Here is the function for you:
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

3) Your TruncateNumber function is correct. Here is the function for you:
func TruncateNumber(number float64) float64 {
    return math.Mod(number, 1)
}

4) Your Compare function is correct. Here is the function for you:
func Compare(game, guess []int) []int {
    result := make([]int, 0)

    for i := 0; i < len(game); i++ {
        result = append(result, int(math.Abs(float64(game[i]-guess[i]))))
    }

    return result
}