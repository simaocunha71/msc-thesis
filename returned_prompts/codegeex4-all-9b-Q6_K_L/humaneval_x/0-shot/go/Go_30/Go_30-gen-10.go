func GetPositive(l []int) []int {
    res := make([]int, 0, len(l))
    for _, i := range l {
        if i > 0 {
            res = append(res, i)
        }
    }
    return res
}