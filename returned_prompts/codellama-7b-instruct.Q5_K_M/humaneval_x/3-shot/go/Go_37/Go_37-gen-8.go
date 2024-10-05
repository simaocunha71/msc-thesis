    sorted := make([]int, len(l))
    copy(sorted, l)
    sort.Ints(sorted)

    for i := 0; i < len(l); i += 2 {
        if sorted[i] != l[i] {
            sorted[i] = l[i]
        }
    }
    return sorted
}



