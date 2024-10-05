
I have a few comments on your code:

In the first question, you can simplify the function to only have one for loop:
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers)-1; i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}

In the second question, you can simplify the function to only have one for loop:
func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    depth := 0

    for _, c := range paren_string {
        if c == '(' {
            depth += 1
            current_string = append(current_string, c)
        } else if c == ')' {
            depth -= 1
            current_string = append(current_string, c)

            if depth == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        }
    }
    return result
}

In the third question, you can simplify the function to only have one for loop:
func TruncateNumber(number float64) float64 {
    return number - math.Floor(number)
}

In the fourth question, you can simplify the function to only have one for loop:
func SortedListSum(lst []string) []string {
    result := make([]string, 0)
    for _, v := range lst {
        if len(v)%2 == 0 {
            result = append(result, v)
        }
    }
    sort.Strings(result)
    return result
}

I hope this helps!