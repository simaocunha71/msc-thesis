
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
    return math.Mod(number, 1)
}

func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    var result []int
    for i := 0; i < len(lst); i++ {
        if lst[i] != lst[i+1] {
            result = append(result, lst[i])
        }
    }
    if len(result) < 2 {
        return nil
    }
    return result[1]
}