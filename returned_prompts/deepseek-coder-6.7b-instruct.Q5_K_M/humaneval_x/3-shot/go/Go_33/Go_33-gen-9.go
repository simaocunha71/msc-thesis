    sorted := make([]int, len(l))
    copy(sorted, l)
    sort.Ints(sorted)

    for i, v := range sorted {
        if (i+1)%3 == 0 {
            l[(i+1)%len(l)] = v
        }
    }
    return l
}


