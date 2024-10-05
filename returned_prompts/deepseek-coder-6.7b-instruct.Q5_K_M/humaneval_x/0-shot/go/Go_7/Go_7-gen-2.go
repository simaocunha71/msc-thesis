import (
    "strings"
)

func FilterBySubstring(stringList []string, substring string) []string {
    var result []string
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            result = append(result, str)
        }
    }
    return result
}


