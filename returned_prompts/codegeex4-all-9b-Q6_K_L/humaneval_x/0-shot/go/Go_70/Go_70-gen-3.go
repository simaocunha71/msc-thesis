func StrangeSortList(lst []int) []int {
    if len(lst) == 0 {
        return lst
    }
    sorted := make([]int, len(lst))
    copy(sorted, lst)
    sort.Ints(sorted)
    result := make([]int, len(lst))
    i, j := 0, len(sorted)-1
    for k := 0; k < len(lst); k++ {
        if k%2 == 0 {
            result[k] = sorted[i]
            i++
        } else {
            result[k] = sorted[j]
            j--
        }
    }
    return result
}

