
HasCloseElements
Your code is good, but it can be optimized using a single loop and a map to keep track of the numbers you've seen so far. This way, you don't have to compare each number with all the others.
func HasCloseElements(numbers []float64, threshold float64) bool {
    seen := make(map[float64]bool)
    for _, num := range numbers {
        for seenNum := range seen {
            if math.Abs(num-seenNum) < threshold {
                return true
            }
        }
        seen[num] = true
    }
    return false
}

SeparateParenGroups
Your code is good, but it can be optimized by removing the need to convert the slice of runes to a string when appending it to the result. Instead, you can append the runes directly to the result.
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
Your code is good, but it can be optimized by using the math.Trunc function instead of math.Mod. This is because math.Trunc will return the integer part of the number, which is what you want.
func TruncateNumber(number float64) float64 {
    return math.Trunc(number)
}

GetMaxTriples
Your code is good, but it can be optimized by using a single loop and a map to keep track of the numbers you've seen so far. This