    sort.Ints(l1)
    sort.Ints(l2)

    i, j, common := 0, 0, make([]int, 0)

    for i < len(l1) && j < len(l2) {
        if l1[i] == l2[j] {
            common = append(common, l1[i])
            i++
            j++
        } else if l1[i] < l2[j] {
            i++
        } else {
            j++
        }
    }

    return common
}



