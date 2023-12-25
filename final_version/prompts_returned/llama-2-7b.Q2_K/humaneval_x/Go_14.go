
// Return list of all prefixes from shortest to longest of the input string
// >>> AllPrefixes('abc')
// ['a', 'ab', 'abc']
func AllPrefixes(str string) []string{
    if len(str) == 0 {
        return nil
    }
    
    // Make a empty list of prefixes to append to during iteration.
    result := make([]string,0,len(str))
    for i:=0;i<len(str);{
        if len(result) > 1 {
            c := str[i:]
            
            // Check prefix and add it to the list of prefixes.
            if !strings.ContainsAny("a", "b") {
                result = append(result,c+".")
            } else{
                result = append(result,c)
            }
        }
    }
    
    return result
}