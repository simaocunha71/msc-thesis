// Out of list of strings, return the Longest one. Return the first one in case of multiple
// strings of the same length. Return nil in case the input list is empty.
// >>> Longest([])
// nil
// >>> Longest(['a', 'b', 'c'])
// 'a'
// >>> Longest(['a', 'bb', 'ccc'])
// 'ccc'
func Longest(strings []string) interface{} {
    if len(strings) == 0 {
        return nil
    }
    longest := strings[0]
    for _, s := range strings[1:] {
        if len(s) > len(longest) {
            longest = s
        }
    }
    return longest
}

// Out of list of strings, return the Longest one. Return the first one in case of multiple
// strings of the same length. Return nil in case the input list is empty.
// >>> Longest([])
// nil
// >>> Longest(['a', 'b', 'c'])
// 'a'
// >>> Longest(['a', 'bb', 'ccc'])
// 'ccc'
func Longest(strings []string) interface{} {
    if len(strings) == 0 {
        return nil
    }
    longest := strings[0]
    for _, s := range strings[1:] {
        if len(s) > len(longest) {
            longest = s
        }
    }
    return longest
}

// Out of list of strings, return the Longest one. Return the first one in case of multiple
// strings of the same length. Return nil in case the input list is empty.
// >>> Longest([])
// nil
// >>> Longest(['a', 'b', 'c'])
// 'a'
// >>> Longest(['a', 'bb', 'ccc'])
// 'ccc'
func Longest(strings []string) interface{} {
    if len(strings) == 0 {
        return nil
    }
    longest := strings[0]
    for _, s := range strings[1:] {
        if len(s) > len(longest) {
            longest = s
        }
    }
    return longest
}

// Out