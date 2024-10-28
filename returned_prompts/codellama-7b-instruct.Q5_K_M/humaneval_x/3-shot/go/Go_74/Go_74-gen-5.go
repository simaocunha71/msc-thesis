    var result []string

    for _, s1 := range lst1 {
        for _, s2 := range lst2 {
            if len(s1) < len(s2) {
                result = append(result, s1)
                break
            }
        }
    }
    return result
}



