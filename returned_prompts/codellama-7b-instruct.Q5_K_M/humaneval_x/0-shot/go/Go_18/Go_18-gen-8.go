
// Find the first occurrence of the substring in the original string.
// >>> FindFirst('', 'a')
// -1
// >>> FindFirst('aaa', 'a')
// 0
// >>> FindFirst('aaaa', 'aa')
// 0
func FindFirst(str string,substring string) int{

B:

// Find the first occurrence of the substring in the original string, starting from a given index.
// >>> FindFrom('', 'a', 0)
// -1
// >>> FindFrom('aaa', 'a', 0)
// 0
// >>> FindFrom('aaaa', 'aa', 0)
// 0
// >>> FindFrom('aaaa', 'aa', 1)
// 2
func FindFrom(str string,substring string,from int) int{

C:

// Find the last occurrence of the substring in the original string.
// >>> FindLast('', 'a')
// -1
// >>> FindLast('aaa', 'a')
// 2
// >>> FindLast('aaaa', 'aa')
// 2
func FindLast(str string,substring string) int{

D:

// Find the last occurrence of the substring in the original string, starting from a given index.
// >>> FindLastFrom('', 'a', 0)
// -1
// >>> FindLastFrom('aaa', 'a', 0)
// 2
// >>> FindLastFrom('aaaa', 'aa', 0)
// 2
// >>> FindLastFrom('aaaa', 'aa', 1)
// 2
// >>> FindLastFrom('aaaa', 'aa', 2)
// 0
func FindLastFrom(str string,substring string,from int) int{

E:

// Replace all occurrences of the substring with a replacement string.
// >>> ReplaceAll('', 'a', 'b')
// ''
// >>> ReplaceAll('aaa', 'a', 'b')
// 'bbb'
// >>> ReplaceAll('aaaa', 'aa', 'b')
// 'bbbb'
func ReplaceAll(str string,substring string,replacement string) string{

F:

// Replace the first occurrence of the substring with a replacement string.
