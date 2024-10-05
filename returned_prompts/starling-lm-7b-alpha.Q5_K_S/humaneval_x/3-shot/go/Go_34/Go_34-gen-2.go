    result := make([]int, 0)
    l_sort := make([]int, 0)

    for _, v := range l {
        l_sort = append(l_sort, v)
    }
    sort.Ints(l_sort)

    prev := 0
    for _, v := range l_sort {
        if v != prev {
            result = append(result, v)
            prev = v
        }
    }
    return result
}



