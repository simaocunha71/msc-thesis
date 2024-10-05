func GetPositive(l []int) []int {
    var p []int
    for _, v := range l {
        if v > 0 {
            p = append(p, v)
        }
    }
    return p
}