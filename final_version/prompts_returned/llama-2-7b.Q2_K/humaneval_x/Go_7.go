import (
    "strings"
)

// Filter an input list of strings only for ones that contain given substring
// >>> FilterBySubstring([], 'a')
// []
// >>> FilterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')
// ['abc', 'bacd', 'array']
func FilterBySubstring(stringList []string, substring string) []string {
    newStringList := make([]string, 0, len(stringList))
    for _, v := range stringList {
        if strings.Contains(v, substring) {
            // If substring is found in the input value, add it to newly created array of values
            // Note that we are using the default capitalization for the case-insensitive search and the substring matches are not necessarily ordered properly either!
            newStringList = append(newStringList, strings.ToLower(v))
        }
    }
    return newStringList
}