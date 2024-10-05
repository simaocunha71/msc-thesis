import (
    "strings"
)

// Filter an input list of strings only for ones that contain given substring
// >>> FilterBySubstring([], 'a')
// []
// >>> FilterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')
// ['abc', 'bacd', 'array']
func FilterBySubstring(stringList []string, substring string) []string {
    var filteredList []string
    for _, s := range stringList {
        if strings.Contains(s, substring) {
            filteredList = append(filteredList, s)
        }
    }
    return filteredList
}

