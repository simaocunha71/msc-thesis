
// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {
    var output []string
    for i, c := range paren_string {
        switch c {
          case ')':
            if i == 0 {
                break
             }
         }
        switch c {
          case '(':
           if i == 0 {
              continue
           } else {
               output = append(output,paren_string[:i])
               break
           }
       case ')':
            output = append(output,paren_string[:i])
            
         default:
          }
    }
  return output
}