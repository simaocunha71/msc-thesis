    sort.Ints(lst)
    result := make([]int, 0)

    for len(lst) > 0 {
        result = append(result, lst[0])
        lst = lst[1:]
        if len(lst) > 0 {
            result = append(result, lst[len(lst)-1])
            lst = lst[:len(lst)-1]
        }
    }
    return result
}



