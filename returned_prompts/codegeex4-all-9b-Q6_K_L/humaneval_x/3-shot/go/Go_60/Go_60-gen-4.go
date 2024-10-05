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
}

// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := make