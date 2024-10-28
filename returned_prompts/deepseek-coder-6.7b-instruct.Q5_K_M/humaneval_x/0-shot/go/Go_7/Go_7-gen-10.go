    var filteredList  []string
    for _, value := range stringList {
        if strings.Contains(value, substring) {
            filteredList = append(filteredList, value)
        }
    }
    return filteredList
}


A: Here is the corrected version of your code.

