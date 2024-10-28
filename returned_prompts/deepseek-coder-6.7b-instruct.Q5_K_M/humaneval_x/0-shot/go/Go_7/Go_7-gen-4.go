func FilterBySubstring(stringList []string, substring string) []string {
    result := make([]string, 0)
    for _, str := range stringList