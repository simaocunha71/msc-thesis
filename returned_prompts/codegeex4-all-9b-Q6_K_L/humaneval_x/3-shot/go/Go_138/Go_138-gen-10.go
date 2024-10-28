
I would suggest adding some documentation to the functions. It will help someone else (or your future self) to understand what the function is supposed to do.
This is how I would write the functions:
func HasCloseElements(numbers []float64, threshold float64) bool {
    // Check if in given list of numbers, are any two numbers closer to each other than given threshold.
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
    // Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    // separate those group into separate strings and return the list of those.
    // Separate groups are balanced (each open brace is properly closed) and not nested within each other
    // Ignore any spaces in the input string.
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
    // Given a positive floating point number, it can be decomposed into
    // and integer part (largest integer smaller than given number) and decimals
    // (leftover part always smaller than 1).
    //
    // Return the decimal part of the number.
    return math.Mod(number, 1)
}

func IsEqualToSumEven(n int) bool {
    // Evaluate whether the given number n can be written as the sum of exactly