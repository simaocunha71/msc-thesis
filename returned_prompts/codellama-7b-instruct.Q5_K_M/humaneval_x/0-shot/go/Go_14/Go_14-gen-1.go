
// Return list of all prefixes from shortest to longest of the input string
// >>> AllPrefixes('abc')
// ['a', 'ab', 'abc']
func AllPrefixes(str string) []string{
    var prefixes []string
    for len(str) > 0 {
        prefixes = append(prefixes, str)
        str = str[:len(str)-1]
    }
    return prefixes
}
