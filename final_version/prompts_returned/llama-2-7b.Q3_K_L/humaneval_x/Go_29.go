
// Filter an input list of strings only for ones that start with a given prefix.
// >>> FilterByPrefix([], 'a')
// []
// >>> FilterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')
// ['abc', 'array']
func FilterByPrefix(strings []string,prefix string) []string {
    var output []string
    for _, s := range strings{
        if s[:1]==prefix {
            output = append(output,s[1:])
        }
     }
     return output
}
