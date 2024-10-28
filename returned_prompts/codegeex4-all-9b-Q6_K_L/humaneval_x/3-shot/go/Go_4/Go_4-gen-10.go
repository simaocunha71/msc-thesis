
Here are the issues in your code:

In HasCloseElements function, you should use var distance := math.Abs(numbers[i] - numbers[j]) instead of var distance float64 = math.Abs(numbers[i] - numbers[j]).

In MeanAbsoluteDeviation function, you should use Sum(numbers) instead of Sum(numbers[i]). Also, you should use sum, not sum1.

In SeparateParenGroups function, you should use result = append(result, string(current_string)) instead of result = append(result, current_string).

In SeparateParenGroups function, you should use current_string = make([]rune, 0) instead of current_string =  make([]rune, 0).

In SeparateParenGroups function, you should use c == '(' instead of c == '(', and c == ')' instead of c == ')'.

In TruncateNumber function, you should use return math.Mod(number,1) instead of return math.Mod(number,1).

Here is the corrected code:

// Check if in given list of numbers, are any two numbers closer to each other than given threshold.
// >>> HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5)
// false
// >>> HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
// true
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var distance := math.Abs(numbers[i] - numbers[j])
            if distance < threshold {
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
// >>>