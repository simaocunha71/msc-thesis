import (
    "strings"
)

// Filter an input list of strings only for ones that contain given substring
// >>> FilterBySubstring([], 'a')
// []
// >>> FilterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')
// ['abc', 'bacd', 'array']
func FilterBySubstring(stringList []string, substring string) []string {
    filtered := make([]string, 0, len(stringList))
    for _, s := range stringList {
        if strings.Contains(s, substring) {
            filtered = append(filtered, s)
        }
    }

    return filtered
}