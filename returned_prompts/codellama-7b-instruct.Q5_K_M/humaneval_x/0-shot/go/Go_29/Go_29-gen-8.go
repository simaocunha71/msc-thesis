
// Filter an input list of strings only for ones that end with a given suffix.
// >>> FilterBySuffix([], 'a')
// []
// >>> FilterBySuffix(['abc', 'bcd', 'cde', 'array'], 'c')
// ['abc', 'cde']
func FilterBySuffix(strings []string,suffix string) []string {

B:

// Filter an input list of strings only for ones that contain a given word.
// >>> FilterByWord([], 'a')
// []
// >>> FilterByWord(['abc', 'bcd', 'cde', 'array'], 'cd')
// ['bcd', 'cde']
func FilterByWord(strings []string,word string) []string {
