    result := make([]int, len(l))
    copy(result, l)
    for i := range l {
        if i%3 == 0 {
            result[i] = sort.IntSlice(l[i:]).Slice(0,1)[0]
        }
    }
    return result
}



