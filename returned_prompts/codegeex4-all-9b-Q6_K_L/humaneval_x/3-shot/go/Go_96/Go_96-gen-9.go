
The first one is almost good. You just need to return the result before the loop:
func HasCloseElements(numbers []float64, threshold float64) bool {

    result := false
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var distance float64 = math.Abs(numbers[i] - numbers[j])
            if distance < threshold {
                result = true
                return result
            }
        }
    }
    return result
}

The second one is almost good too. You just need to return the result before the loop:
func SeparateParenGroups(paren_string string) []string {

    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_string = append(current_string, c)
        }else if c== ')'{
            current_depth -= 1
            current_string = append(current_string, c)

            if current_depth == 0{
                result = append(result, string(current_string))
                current_string =  make([]rune, 0)
            }
        }

    }
    return result
}

The third one is good. You just need to return the result before the loop:
func TruncateNumber(number float64) float64 {
    return math.Mod(number,1)
}

The fourth one is good. You just need to return the result before the loop:
func CountUpTo(n int) []int {

    result := make([]int, 0)
    for i:= 2; i < n; i++{
        for j:= 2; j < i; j++{
            if i % j == 0{
                break
            }
            if j == i-1{
                result = append(result, i)
            }
        }
    }
    return result
}