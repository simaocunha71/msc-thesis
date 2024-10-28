    var result []string

    if totalChars(lst1) < totalChars(lst2) {
        result = lst1
    } else if totalChars(lst1) > totalChars(lst2) {
        result = lst2
    } else {
        result = lst1
    }

    return result
}

func totalChars(lst []string) int {
    var total int
    for _, s := range lst {
        total += len(s)
    }
    return total
}