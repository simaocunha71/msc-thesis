    if len(lst) < 2 {
        return nil
    }

    sorted := make([]int, len(lst))
    copy(sorted, lst)

    sort.Ints(sorted)

    if sorted[1] == sorted[0] {
        return nil
    }

    return sorted[1]
}



