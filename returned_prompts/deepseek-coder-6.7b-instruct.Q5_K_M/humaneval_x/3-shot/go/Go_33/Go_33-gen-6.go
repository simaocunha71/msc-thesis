    result  := make([]int, len(l))
    copy(result, l)
    sortable  := make([]int, 0)

    for i  := 0; i  len(l); i += 3  {
        sortable = append(sortable, result[i])
    }

    sort.Ints(sortable)

    for i  := 0; i  len(l); i += 3  {
        result[i] = sortable[0]
        sortable = sortable[1:]
    }

    return result
}



