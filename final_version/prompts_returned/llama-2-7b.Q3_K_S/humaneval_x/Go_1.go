
// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {
    groups := strings.Split(paren_string, "(")
    parenArr := make([]string, len(groups))
    n := 0
    
    for i := range groups {
        if groups[i] == "" || !strings.ContainsAny(groups[i], "(", ")") {
            return []string{}
        } else if groups[i] != "()" && groups[i] != ")" {
            parenArr[n] = strings.TrimPrefix(groups[i], "$$")
            n += 1
        }
    }
    
    return parenArr
}
