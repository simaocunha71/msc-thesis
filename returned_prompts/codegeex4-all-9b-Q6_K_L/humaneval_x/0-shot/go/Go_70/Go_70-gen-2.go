func StrangeSortList(lst []int) []int {
    if len(lst) == 0 {
        return lst
    }

    sort.Ints(lst)
    result := make([]int, len(lst))

    left, right := 0, len(lst)-1
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 {
            result[i] = lst[left]
            left++
        } else {
            result[i] = lst[right]
            right--
        }
    }

    return result
}

