import (
    "strings"
)

// Given a string, find out how many distinct characters (regardless of case) does it consist of
// >>> CountDistinctCharacters('xyzXYZ')
// 3
// >>> CountDistinctCharacters('Jerry')
// 4
func CountDistinctCharacters(str string) int{
    // Replace all characters to lower case
    str = strings.ToLower(str)
    // Create a map of characters
    // Count the number of characters in the map
    return len(map[string]bool(str))
}

