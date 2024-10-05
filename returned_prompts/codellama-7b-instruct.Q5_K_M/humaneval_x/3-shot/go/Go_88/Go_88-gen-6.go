    result := make([]int, len(array))
    copy(result, array)

    sort.Ints(result)

    if sum(result[0], result[len(result)-1])%2 == 0 {
        sort.Ints(result)
    }else {
        sort.Sort(sort.Reverse(sort.IntSlice(result)))
    }
    return result
}



