
Your solutions are generally good, but there are a few improvements that could be made:

In the HasCloseElements function, you can simplify the logic by using a single loop and checking the absolute difference between each pair of numbers.
In the SeparateParenGroups function, you can simplify the logic by using a stack to keep track of the current depth and the current string.
In the TruncateNumber function, you can simplify the logic by using the built-in math.Floor function.
In the IsHappy function, you can simplify the logic by using a set to keep track of the last two characters.

Here's the updated code:

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

func IsHappy(s string) bool {
    if len(s) < 3 {
        return false
    }

    last_two := make(map[rune]bool)
    for i := 0; i < len(s)-2; i++ {
        if _, ok := last_two[s[i]]; ok {
            return false
        }
        last_two[s[i