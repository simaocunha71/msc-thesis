
The first function you posted seems correct, but it could be more readable if you use the more idiomatic syntax for range loops in Go:

// Check if in given list of numbers, are any two numbers closer to each other than given threshold.
// >>> HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5)
// false
// >>> HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
// true
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i, x := range numbers {
        for j, y := range numbers {
            if i != j && math.Abs(x-y) < threshold {
                return true
            }
        }
    }
    return false
}

The second function seems correct, but it could be more efficient if you only iterate over the characters in the string once, and keep track of the depth as you go:

// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {
    result := make([]string