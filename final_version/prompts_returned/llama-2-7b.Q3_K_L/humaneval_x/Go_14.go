
// Return list of all prefixes from shortest to longest of the input string
// >>> AllPrefixes('abc')
// ['a', 'ab', 'abc']
func AllPrefixes(str string) []string{
    var (
        result []string
        i int
        ch   byte
    )
    
    for i = 0; i < len(str); i++ {
        ch = str[i]
        if (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'){
            result = append(result, []byte{ch})
        } else {
            break;
        }
    }
    
    return result
}

// Return list of all suffixes from longest to shortest of the input string
// >>> AllSuffixes('abc')
// ['bc', 'ca']
func AllSuffixes(str string) []string{
    var (
        result []string
        i int
        ch   byte
    )
    
    for i = len(str) - 1; i >=0; i-- {
        ch = str[i]
        if (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'){
            result = append(result, []byte{ch})
        } else {
            break;
        }
    }
    
    return result
}
