    even := make([]int, 0, len(l)/2+1)
    for i := 0; i < len(l); i += 2 {
        even = append(even, l[i])
    }
    sort.Ints(even)
    result := make([]int, len(l))
    for i, j := 0, 0; i < len(l); i += 2 {
        result[i] = even[j]
        j++
    }
    for i := 1; i < len(l); i += 2 {
        result[i] = l[i]
    }
    return result
}



