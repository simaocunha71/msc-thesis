
import "math"

// Check if in given list of numbers, are any two numbers closer to each other than given threshold.
// >>> HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5)
// false
// >>> HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
// true
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i, n := range numbers {
        for _, m := range numbers[i+1:] {
            if math.Abs(n-m) <= threshold {
                return true
            }
        }
    }
    return false
}

// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {
    var result []string
    var buffer []rune
    depth := 0

    for _, c := range paren_string {
        if c == '(' {
            depth++
            buffer = append(buffer, c)
        } else if c == ')' {
            depth--
            buffer = append(buffer, c)
            if depth == 0 {
                result = append(result, string(buffer))
                buffer = nil
            }
        }
    }
    return result
}

// Given a positive floating point number, it can be decomposed into
// and integer part (largest integer smaller than given number) and decimals
// (leftover part always smaller than 1).
// 
// Return the decimal part of the number.
// >>> TruncateNumber(3.5)
// 0.5
func TruncateNumber(number float64) float64 {
    return number - math.Floor(number)
}

// Filter an input list of strings only for ones that start with a given prefix.
// >>> Filter