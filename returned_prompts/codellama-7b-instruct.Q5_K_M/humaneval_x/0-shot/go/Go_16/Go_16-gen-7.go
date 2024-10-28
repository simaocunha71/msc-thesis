import (
    "strings"
)

// Given a string, find out how many distinct characters (regardless of case) does it consist of
// >>> CountDistinctCharacters('xyzXYZ')
// 3
// >>> CountDistinctCharacters('Jerry')
// 4
func CountDistinctCharacters(str string) int{

    // Create a map of all characters
    m := make(map[string]bool)
    for _, c := range str {
        m[strings.ToLower(string(c))] = true
    }

    // Return the length of the map
    return len(m)
}
