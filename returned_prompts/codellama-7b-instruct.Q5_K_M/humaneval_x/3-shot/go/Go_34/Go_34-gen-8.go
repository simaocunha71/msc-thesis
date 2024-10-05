    sort.Ints(l)
    result := make([]int, 0)
    for _, i := range l {
        if len(result) == 0 || result[len(result)-1] != i {
            result = append(result, i)
        }
    }
    return result
}



