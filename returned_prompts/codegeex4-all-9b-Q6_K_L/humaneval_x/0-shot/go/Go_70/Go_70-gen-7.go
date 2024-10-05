func StrangeSortList(lst []int) []int {
    if len(lst) < 2 {
        return lst
    }
    sort.Ints(lst)
    res := make([]int, 0, len(lst))
    left := 0
    right := len(lst) - 1
    for left <= right {
        res = append(res, lst[left])
        if left != right {
            res = append(res, lst[right])
        }
        left++
        right--
    }
    return res
}