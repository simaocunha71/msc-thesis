
// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {

    var groups []string
    var currentGroup string
    var depth int

    for i, c := range paren_string {
        switch c {
        case '(':
            depth++
            currentGroup += c
        case ')':
            depth--
            currentGroup += c
            if depth == 0 {
                groups = append(groups, currentGroup)
                currentGroup = ""
            }
        }
    }

    return groups
}
