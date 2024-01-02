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
    var res string // result variable
    var maxLen int = 0

    for _, str := range strings {
        // Get the length of each string.
        length := len(str)
        // If the length is longer than the existing one, set it.
        if length > maxLen {
            maxLen = length
        }
    }

    res = strings[0]
    for _, str := range strings {
        // Get the length of each string again
        length := len(str)
        // If the length is longer, compare with the existing one and return it.
        if length > maxLen && length == maxLen {
            res = str
        }
    }
    return res
}
