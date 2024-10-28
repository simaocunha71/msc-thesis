func FilterBySubstring(stringList []string, substring string) []string {
    var outputList []string
    for _, element := range stringList {
        if strings.Contains(element, substring) {
            outputList = append(outputList, element)
        }
    }
    return outputList
}

