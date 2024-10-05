
// Filter an input list of strings only for ones that end with a given suffix.
// >>> FilterBySuffix([], 'a')
// []
// >>> FilterBySuffix(['abc', 'bcd', 'cde', 'array'], 'y')
// ['array']
func FilterBySuffix(strings []string,suffix string) []string {

B:

// Filter an input list of strings only for ones that contain a given substring.
// >>> FilterBySubstring([], 'a')
// []
// >>> FilterBySubstring(['abc', 'bcd', 'cde', 'array'], 'cd')
// ['bcd', 'cde']
func FilterBySubstring(strings []string,substring string) []string {

C:

// Filter an input list of strings only for ones that have a given length.
// >>> FilterByLength([], 3)
// []
// >>> FilterByLength(['abc', 'bcd', 'cde', 'array'], 4)
// ['bcd', 'cde']
func FilterByLength(strings []string,length int) []string {

D:

// Filter an input list of strings only for ones that are equal to a given string.
// >>> FilterByValue([], 'a')
// []
// >>> FilterByValue(['abc', 'bcd', 'cde', 'array'], 'array')
// ['array']
func FilterByValue(strings []string,value string) []string {

E:

// Filter an input list of strings only for ones that are not equal to a given string.
// >>> FilterNotByValue([], 'a')
// []
// >>> FilterNotByValue(['abc', 'bcd', 'cde', 'array'], 'array')
// ['abc', 'bcd', 'cde']
func FilterNotByValue(strings []string,value string) []string {

F:

// Filter an input list of strings only for ones that are not equal to any strings in a given list.
// >>> FilterNotByValues([], ['a', 'b', 'c'])
// []
// >>> FilterNotByValues(['abc', 'bcd', 'cde', 'array'], ['array', 'bcd', 'c