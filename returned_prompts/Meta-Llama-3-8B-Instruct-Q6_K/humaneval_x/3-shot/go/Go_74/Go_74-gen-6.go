    total_chars1 := 0
    total_chars2 := 0
    for _, s := range lst1 {
        total_chars1 += len(s)
    }
    for _, s := range lst2 {
        total_chars2 += len(s)
    }
    if total_chars1 < total_chars2 {
        return lst1
    } else if total_chars1 > total_chars2 {
        return lst2
    } else {
        return lst1
    }
}