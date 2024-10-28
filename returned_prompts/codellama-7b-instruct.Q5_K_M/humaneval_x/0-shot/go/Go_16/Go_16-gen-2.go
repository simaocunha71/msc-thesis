import (
    "strings"
)

// Given a string, find out how many distinct characters (regardless of case) does it consist of
// >>> CountDistinctCharacters('xyzXYZ')
// 3
// >>> CountDistinctCharacters('Jerry')
// 4
func CountDistinctCharacters(str string) int{

    var distinctCharacters = map[string]bool{}
    for _, char := range str {
        distinctCharacters[strings.ToLower(string(char))] = true
    }
    return len(distinctCharacters)
}

