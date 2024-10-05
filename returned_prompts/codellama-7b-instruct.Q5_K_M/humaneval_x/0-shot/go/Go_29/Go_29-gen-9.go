
// Filter an input list of strings only for ones that have length greater than a given length.
// >>> FilterByLength([], 3)
// []
// >>> FilterByLength(['abc', 'bcd', 'cde', 'array'], 3)
// ['abc', 'bcd', 'cde']
func FilterByLength(strings []string,length int) []string {

B:

// Filter an input list of strings only for ones that contain a given substring.
// >>> FilterBySubstring([], 'a')
// []
// >>> FilterBySubstring(['abc', 'bcd', 'cde', 'array'], 'a')
// ['abc', 'bcd', 'cde', 'array']
func FilterBySubstring(strings []string,substring string) []string {

C:

// Filter an input list of strings only for ones that end with a given suffix.
// >>> FilterBySuffix([], 'a')
// []
// >>> FilterBySuffix(['abc', 'bcd', 'cde', 'array'], 'a')
// ['abc', 'cde', 'array']
func FilterBySuffix(strings []string,suffix string) []string {

D:

// Find all the strings in a list of strings that have a given prefix, then return them in alphabetical order.
// >>> FindByPrefix([], 'a')
// []
// >>> FindByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')
// ['abc', 'array']
func FindByPrefix(strings []string,prefix string) []string {

E:

// Find all the strings in a list of strings that have a given suffix, then return them in alphabetical order.
// >>> FindBySuffix([], 'a')
// []
// >>> FindBySuffix(['abc', 'bcd', 'cde', 'array'], 'a')
// ['abc', 'cde', 'array']
func FindBySuffix(strings []string,suffix string) []string {

F:

// Find all the strings in a list of strings that have a given substring, then return them in alphabetical order.
// >>> FindBySubstring([], 'a')