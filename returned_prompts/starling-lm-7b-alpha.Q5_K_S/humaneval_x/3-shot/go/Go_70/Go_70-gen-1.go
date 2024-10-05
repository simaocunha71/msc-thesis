    sorted := make([]int, 0)
    for len(lst) > 0 {
        min := math.MaxInt64
        for i := range lst {
            if lst[i] < min {
                min = lst[i]
            }
        }
        sorted = append(sorted, min)
        lst = remove(lst, min)
    }

    sort.Reverse(sorted)
    return sorted
}



