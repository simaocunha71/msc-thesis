    var result []int
    sort.Ints(l1)
    sort.Ints(l2)
    i, j := 0, 0
    for i < len(l1) && j < len(l2) {
        if l1[i] < l2[j] {
            i++
        } else if l1[i] > l2[j] {
            j++
        } else {
            result = append(result, l1[i])
            i++
            j++
        }
    }
    return result
}



