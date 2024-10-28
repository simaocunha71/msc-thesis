    var result []string
    if total_chars(lst1) < total_chars(lst2) {
        result = lst1
    } else if total_chars(lst1) > total_chars(lst2) {
        result = lst2
    } else {
        result = lst1
    }
    return result

}

func total_chars(lst []string) int {
    total := 0
    for _, str := range lst {
        total += len(str)
    }
    return total
}