    result := make([]int, len(l))
    copy(result, l)
    for i := 0; i < len(l); i += 2 {
        result[i] = l[i]
        result[i+1] = sort.IntSlice(l[i+1:i+2]).Sort()
    }
    return result
}



