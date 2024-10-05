    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    unique := make([]int, 0)
    for _, v := range lst {
        if len(unique) == 0 || v != unique[len(unique)-1] {
            unique = append(unique, v)
        }
    }
    if len(unique) < 2 {
        return nil
    }
    return unique[1]
}



