    sort.Ints(l)
    var result []int
    for i, v := range l {
        if i == 0 || v != l[i-1] {
            result = append(result, v)
        }
    }
    return result
}



