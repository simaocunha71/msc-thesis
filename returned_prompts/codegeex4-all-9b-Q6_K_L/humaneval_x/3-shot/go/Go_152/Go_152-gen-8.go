
For the first question, your function is correct. Here is how you can simplify it:
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := range numbers {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}

For the second question, there are a few things you could improve. First, you don't need to use a slice of runes, you can just use a string. Second, you don't need to check if the current depth is 0 after each closing parenthesis, you can check it once after the loop. Third, you can use a more idiomatic way to append to the result slice. Here is how you can simplify it:
func SeparateParenGroups(paren_string string) []string {
    result := []string{}
    current_string := ""
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
        } else if c == ')' {
            current_depth -= 1
            if current_depth == 0 {
                result = append(result, current_string)
                current_string = ""
            }
        } else if current_depth > 0 {
            current_string += string(c)
        }
    }
    return result
}

For the third question, your function is correct. Here is how you can simplify it:
func TruncateNumber(number float64) float64 {
    return math.Mod(number, 1)
}

For the fourth question, there are a few things you could improve. First, you don't need to use a range loop with the index. Second, you can use the math.Abs function directly on the result of the subtraction, you don't need to convert it to a float64 first. Here is how you can simplify it:
func Compare(game, guess []int) []int {
    result := make([]int, len(game))
    for i := range game {
        result[i] = int(math.Abs(float64(game[i] - guess[i])))
    }
    return result
}