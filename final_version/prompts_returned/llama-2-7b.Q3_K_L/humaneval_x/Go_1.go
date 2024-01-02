
// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {
    var stack = make([]int, 0)
    
    for ; len(paren_string) > 0; { // Loop until there are no more parenthesis to parse
        if paren_string[len(paren_string)-1] == '(' || paren_string[len(paren_string)-1] == '{' {
            stack = append(stack, len(paren_string)) // Add open parentheses to the top of our stack
        } else {
            if len(stack) > 0 && stack[len(stack)-1] < len(paren_string){ // Make sure there is an open parenthesis at the top of the list.
                paren_string = paren_string[:len(paren_string)-1] // Remove one character from our string because we found it's matching close parenthesis
            } else {
                return []string{} // Return empty array if we didn't find a match
            }
        }
    }
    
    new_arr := make([]string, 0)
    for len(stack) > 0{ // Loop through each element at the top of our stack to remove it from our array.
        idx := len(paren_string) - (len(stack)+1) // Remove one character that was added if not empty array
        paren_string = append(paren_string, string((stack)[0])+char(idx))
    }
    
    for ; len(paren_string) > 0; { // Loop again to create our final result
        if paren_string[len(paren_string)-1] == '(' || paren_string[len(paren_string