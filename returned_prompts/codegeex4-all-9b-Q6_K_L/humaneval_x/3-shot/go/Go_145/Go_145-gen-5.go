
First thing I would do is add a few comments to your code to make it more readable.
As for the code itself, it looks good, but there are a few minor things I would suggest:

In your HasCloseElements function, you can use a range loop to iterate over the numbers instead of a for loop. This makes the code a bit cleaner:
func HasCloseElements(numbers []float64, threshold float64) bool {
    for _, num1 := range numbers {
        for _, num2 := range numbers {
            if num1 != num2 && math.Abs(num1-num2) < threshold {
                return true
            }
        }
    }
    return false
}

In your SeparateParenGroups function, you can use strings.Builder instead of making a slice of runes. This is more efficient and makes the code cleaner:
func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := strings.Builder{}
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

In your TruncateNumber function, you can use math