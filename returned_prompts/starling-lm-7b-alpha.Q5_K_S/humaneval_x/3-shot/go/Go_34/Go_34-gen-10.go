    l = l[:len(l):len(l)+1]
    sort.Ints(l)
    prev := l[0]
    result := make([]int, 0)
    for _, v := range l {
        if v != prev {
            result = append(result, v)
            prev = v
        }
    }
    return result
}



