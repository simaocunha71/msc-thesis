
// Filter an input list of strings for those that contain a given substring.
// >>> FilterBySubstring([], 'a')
// []
// >>> FilterBySubstring(['abc', 'bcd', 'cde', 'array'], 'cd')
// ['bcd', 'cde']
func FilterBySubstring(strings []string, substring string) []string {

B:

// Filter an input list of strings for those that do not contain a given substring.
// >>> FilterOutSubstring([], 'a')
// []
// >>> FilterOutSubstring(['abc', 'bcd', 'cde', 'array'], 'cd')
// ['abc', 'array']
func FilterOutSubstring(strings []string, substring string) []string {

C:

// Filter an input list of strings for those that do not contain a given substring.
// >>> FilterOutSubstring([], 'a')
// []
// >>> FilterOutSubstring(['abc', 'bcd', 'cde', 'array'], 'cd')
// ['abc', 'array']
func FilterOutSubstring(strings []string, substring string) []string {

D:

// Filter an input list of strings for those that are not in a given list.
// >>> FilterNotIn(['abc', 'bcd', 'cde', 'array'], ['abc', 'bcd', 'array'])
// ['cde']
func FilterNotIn(strings []string, exclude []string) []string {

E:

// Filter an input list of strings for those that are in a given list.
// >>> FilterIn(['abc', 'bcd', 'cde', 'array'], ['abc', 'bcd', 'array'])
// ['abc', 'bcd', 'array']
func FilterIn(strings []string, include []string) []string {

F:

// Filter an input list of strings for those that are in a given list.
// >>> FilterIn(['abc', 'bcd', 'cde', 'array'], 'bcd')
// ['bcd']
func FilterIn(strings []string, include string) []string {

G:

// Filter an input list of strings for those that are not in a given list.
// >>> FilterNotIn(['abc', 'bcd