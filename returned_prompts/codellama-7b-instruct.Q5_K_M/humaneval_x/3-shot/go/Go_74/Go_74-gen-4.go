    var result []string

    if len(lst1) == len(lst2) {
        result = lst1
    } else if len(lst1) < len(lst2) {
        result = lst1
    } else {
        result = lst2
    }

    for _, s1 := range result {
        for _, s2 := range result {
            if len(s1+s2) < len(s2+s1) {
                result = append(result, s1+s2)
            }
        }
    }
    return result
}



