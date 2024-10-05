import (
    "strings"
)

// Given a string, find out how many distinct characters (regardless of case) does it consist of
// >>> CountDistinctCharacters('xyzXYZ')
// 3
// >>> CountDistinctCharacters('Jerry')
// 4
func CountDistinctCharacters(str string) int{
    // Convert the string to lowercase
    str = strings.ToLower(str)

    // Create a map of characters
    charMap := map[string]bool{}

    // Iterate through the string and add the characters to the map
    for _, char := range str {
        charMap[string(char)] = true
    }

    // Return the length of the map
    return len(charMap)
}

