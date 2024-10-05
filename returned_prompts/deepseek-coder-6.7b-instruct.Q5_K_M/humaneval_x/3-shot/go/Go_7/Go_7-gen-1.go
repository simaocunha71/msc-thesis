    filteredList := make([]string, 0)

    for _, str := range stringList {
        if strings.Contains(str, substring) {
            filteredList = append(filteredList, str)
        }
    }

    return filteredList
}



