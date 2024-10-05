    sort.Ints(l)
    var result []int
    for _, e := range l {
        if len(result) == 0 || result[len(result)-1] != e {
            result = append(result, e)
        }
    }
    return result
}



