
Your first function is almost correct, but you forgot to break out of the outer loop when a pair of elements is found:
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

Your second function is correct, but it could be simplified by using a stack to keep track of the current depth of parentheses. This would make it easier to handle nested parentheses correctly:
func SeparateParenGroups(paren_string string) []string {
    result := []string{}
    stack := []rune{}
    current_string := ""

    for _, c := range paren_string {
        if c == '(' {
            stack = append(stack, c)
            current_string += string(c)
        } else if c == ')' {
            stack = stack[:len(stack)-1]
            current_string += string(c)
            if len(stack) == 0 {
                result = append(result, current_string)
                current_string = ""
            }
        }
    }
    return result
}

Your third function is correct, but it could be simplified by using the built-in math.Floor function:
func TruncateNumber(number float64) float64 {
    return number - math.Floor(number)
}

Your fourth function is correct, but it could be simplified by using a for loop to iterate over the grid and summing up the number of wells that contain water:
func MaxFill(grid [][]int, capacity int) int {
    result := 0
    for _, row := range grid {
        for _, well := range row {
            if well == 1 {
                result += capacity
            }
        }
    }
    return result
}