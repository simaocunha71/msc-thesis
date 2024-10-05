func StrangeSortList(lst []int) []int {
    sort.Ints(lst)
    var result []int
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 {
            result = append(result, lst[i/2])
        } else {
            result = append(result, lst[len(lst)-(i/2)-1])
        }
    }
    return result
}

