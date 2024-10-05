
// Filter an input list of strings only for ones that end with a given suffix.
// >>> FilterBySuffix([], 'a')
// []
// >>> FilterBySuffix(['abc', 'bcd', 'cde', 'array'], 'a')
// ['abc', 'cde']
func FilterBySuffix(strings []string, suffix string) []string {

B:

// Filter an input list of strings only for ones that contain a given substring.
// >>> FilterBySubstring([], 'a')
// []
// >>> FilterBySubstring(['abc', 'bcd', 'cde', 'array'], 'a')
// ['abc', 'bcd', 'cde', 'array']
func FilterBySubstring(strings []string, substring string) []string {

C:

// Filter an input list of strings only for ones that contain a given substring.
// >>> FilterBySubstring([], 'a')
// []
// >>> FilterBySubstring(['abc', 'bcd', 'cde', 'array'], 'a')
// ['abc', 'bcd', 'cde', 'array']
func FilterBySubstring(strings []string, substring string) []string {

D:

// Find the first element in a list that satisfies a predicate.
// >>> FindFirst([], func(string) bool { return false })
// false
// >>> FindFirst(['abc', 'bcd', 'cde', 'array'], func(string) bool { return false })
// false
func FindFirst(strings []string, predicate func(string) bool) []string {

E:

// Find the first element in a list that satisfies a predicate.
// >>> FindFirst([], func(string) bool { return false })
// false
// >>> FindFirst(['abc', 'bcd', 'cde', 'array'], func(string) bool { return false })
// false
func FindFirst(strings []string, predicate func(string) bool) []string {

F:

// Find the last element in a list that satisfies a predicate.
// >>> FindLast([], func(string) bool { return false })
// false
// >>> FindLast(['abc', 'bcd', 'cde', 'array'], func(string) bool