func GetPositive(l []int) []int {
    var positive []int
    for _, i := range l {
        if i > 0 {
            positive = append(positive, i)
        }
    }
    return positive
}