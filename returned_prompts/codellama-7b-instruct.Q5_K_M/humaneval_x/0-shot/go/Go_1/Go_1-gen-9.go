
// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {
    var result []string

    // Find the first open paren.
    open_paren_idx := strings.IndexRune(paren_string, '(')
    if open_paren_idx == -1 {
        // No open parens.
        return []string{paren_string}
    }

    for {
        // Find the closing paren.
        close_paren_idx := strings.IndexRune(paren_string[open_paren_idx:], ')')
        if close_paren_idx == -1 {
            // Unbalanced string.
            return []string{paren_string}
        }

        // Add the string up to the open paren to the result.
        result = append(result, paren_string[:open_paren_idx])

        // Add the string between the open and close parens to the result.
        result = append(result, paren_string[open_paren_idx:open_paren_idx+close_paren_idx])

        // Remove the just processed string from the input.
        paren_string = paren_string[open_paren_idx+close_paren_idx:]

        // Find the next open paren.
        open_paren_idx = strings.IndexRune(paren_string, '(')
        if open_paren_idx == -1 {
            // No more open parens.
            result = append(result, paren_string)
            break
        }
    }

    return result
}

