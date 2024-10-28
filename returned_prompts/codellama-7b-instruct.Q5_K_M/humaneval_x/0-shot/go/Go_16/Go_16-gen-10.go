import (
    "strings"
)

// Given a string, find out how many distinct characters (regardless of case) does it consist of
// >>> CountDistinctCharacters('xyzXYZ')
// 3
// >>> CountDistinctCharacters('Jerry')
// 4
func CountDistinctCharacters(str string) int{
    var c = make(map[string]bool)
    for _, v := range str {
        c[strings.ToLower(string(v))] = true
    }
    return len(c)
}
