// Out of list of strings, return the Longest one. Return the first one in case of multiple
// strings of the same length. Return nil in case the input list is empty.
// >>> Longest([])
// nil
// >>> Longest(['a', 'b', 'c'])
// 'a'
// >>> Longest(['a', 'bb', 'ccc'])
// 'ccc'
func Longest(strings []string) interface{}{
	if len(strings) == 0 {
		return nil
	}
	maxLength := 0
	var longest string
	for _, s := range strings {
		if len(s) > maxLength {
			maxLength = len(s)
			longest = s
		}
	}
	return longest
}

